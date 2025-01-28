# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

# Data Load & read Data
# Load data
titles = pd.read_csv('/content/titles.csv')
credits = pd.read_csv('/content/credits.csv')

# Cek struktur data
print(titles.info())
print(credits.info())

# Data Cleaning
print("\n## Tahapan Data Cleaning")

def parse_genres(genre_str):
    if isinstance(genre_str, str):
        if pd.isna(genre_str) or genre_str == '[]':
            return []
        genres = genre_str.strip("[]").replace("'", "").replace('"', "").split(',')
        return [g.strip() for g in genres if g.strip() != '']
    elif isinstance(genre_str, list):
        return genre_str
    else:
        return []

# Terapkan ke kolom genres
titles['genres'] = titles['genres'].fillna('[]').apply(parse_genres)
titles['description'] = titles['description'].fillna('')
titles['imdb_score'] = titles['imdb_score'].fillna(0)

# Filter hanya film (bukan TV Show)
movies = titles[titles['type'] == 'MOVIE'].copy()

# Ambil nama aktor dan direktor dari credits
credits['role'] = credits['role'].str.upper()
actors = credits[credits['role'] == 'ACTOR'].groupby('id')['name'].apply(list).reset_index()
directors = credits[credits['role'] == 'DIRECTOR'].groupby('id')['name'].apply(list).reset_index()

# Gabungkan data aktor dan direktor ke movies
movies = movies.merge(actors, on='id', how='left').rename(columns={'name': 'actors'})
movies = movies.merge(directors, on='id', how='left').rename(columns={'name': 'directors'})
    

# Exploratory Data Analysis
# Distibusi Genre
genres_count = movies['genres'].explode().value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=genres_count.values, y=genres_count.index, palette='viridis')
plt.title('Distibusi Genre Film')

# Data Preprocessing & Data Preparation
# Data Preprocessing
movies['actors'] = movies['actors'].fillna('').apply(lambda x: ' '.join(x) if isinstance(x, list) else '')
movies['directors'] = movies['directors'].fillna('').apply(lambda x: ' '.join(x) if isinstance(x, list) else '')
movies['features'] = (
    movies['genres'].astype(str) + ' ' +
    movies['description'] + ' ' +
    movies['actors'] + ' ' +
    movies['directors']
)

# TF-IDF Vectorization
print("\n## Tahapan Ekstraksi Fitur dengan TF-IDF")
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(movies['features'])

# Model Development 
# Hitung Similarity Matrix & Fungsi Rekomendasi
# Hitung Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation Function
def get_recommendations(title, top_n=10):
    try:
        idx = movies[movies['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_indices = [i[0] for i in sim_scores[1:top_n+1]]
        recommendations = movies.iloc[sim_indices][['title', 'genres', 'imdb_score', 'actors', 'directors']]
        recommendations['similarity_score'] = [i[1] for i in sim_scores[1:top_n+1]]
        return recommendations
    except:
        return 'Film tidak ditemukan dalam database'

# evaluasi Model
# Example Evaluation
print("\nHasil Rekomendasi")
recommendations = get_recommendations('Naruto Shippuden the Movie', top_n=10)

# Markdown Table
print("\nHasil Rekomendasi untuk 'Naruto Shippuden the Movie':")
print(recommendations[['title', 'genres', 'imdb_score', 'directors', 'similarity_score']].to_markdown())

# Evaluation Metrics
def evaluate_recommendations(target_title, k=10):
    target_idx = movies[movies['title'] == target_title].index[0]
    sim_scores = list(enumerate(cosine_sim[target_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_indices = [i[0] for i in sim_scores[1:k+1]]
    target_genres = set(movies.iloc[target_idx]['genres'])

    precision = 0
    recall = 0
    relevant_count = 0

    for idx in sim_indices:
        recommended_genres = set(movies.iloc[idx]['genres'])
        if target_genres.intersection(recommended_genres):
            relevant_count += 1

    precision = relevant_count / k if k else 0
    recall = relevant_count / len(target_genres) if target_genres else 0

    return {'precision@k': precision, 'recall@k': recall}

# Evaluasi untuk film 'Naruto Shippuden the Movie'
metrics = evaluate_recommendations('Naruto Shippuden the Movie', k=10)
print("\nEvaluasi Rekomendasi:")
print(f"Precision@10: {metrics['precision@k']:.2f}")
print(f"Recall@10: {metrics['recall@k']:.2f}")

# save Model
pickle.dump(tfidf, open('tfidf_model.pkl', 'wb'))
pickle.dump(cosine_sim, open('cosine_sim.pkl', 'wb'))
