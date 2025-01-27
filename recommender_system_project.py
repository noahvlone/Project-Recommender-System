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
def parse_genres(genre_str):
    # Check if genre_str is a string before attempting strip
    if isinstance(genre_str, str):
        if pd.isna(genre_str) or genre_str == '[]':
            return []
        # Hilangkan tanda kutip dan kurung, lalu split berdasarkan koma
        genres = genre_str.strip("[]").replace("'", "").replace('"', "").split(',')
        return [g.strip() for g in genres if g.strip() != '']
    # If genre_str is already a list, return it as is
    elif isinstance(genre_str, list):
        return genre_str
    else:
        return []
    
# Terapkan ke kolom genres
titles['genres'] = titles['genres'].fillna('[]').apply(parse_genres)

# Handle deskripsi kosong
titles['description'] = titles['description'].fillna('')

# Handle IMDb score kosong
titles['imdb_score'] = titles['imdb_score'].fillna(0)

# Filter hanya film (bukan TV Show)
movies = titles[titles['type'] == 'MOVIE'].copy()

# Ambil nama aktor dan direktor dari credits
credits['role'] = credits['role'].str.upper()
actors = credits[credits['role'] == 'ACTOR'].groupby('id')['name'].apply(list).reset_index()
directors = credits[credits['role'] == 'DIRECTOR'].groupby('id')['name'].apply(list).reset_index()

# Gabungkan ke movies
movies = movies.merge(actors, on='id', how='left').rename(columns={'name': 'actors'})
movies = movies.merge(directors, on='id', how='left').rename(columns={'name': 'directors'})

# Cek contoh genres setelah cleaning
print(movies['genres'].head())

# Exploratory Data Analysis
# Distibusi Genre
genres_count = movies['genres'].explode().value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=genres_count.values, y=genres_count.index, palette='viridis')
plt.title('Distibusi Genre Film')

# Distribusi IMDb score
plt.figure(figsize=(10, 5))
sns.histplot(movies['imdb_score'].dropna(), bins=20, kde=True)
plt.title('Distribusi IMDb Score')

# Data Preprocessing & Data Preparation
# Gabungkan fitur: genre + deskripsi + aktor + direktor
movies['actors'] = movies['actors'].fillna('').apply(lambda x: ' '.join(x) if isinstance(x, list) else '')
movies['directors'] = movies['directors'].fillna('').apply(lambda x: ' '.join(x) if isinstance(x, list) else '')

# Gabungkan semua fitur teks
movies['features'] = (
    movies['genres'].astype(str) + ' ' +
    movies['description'] + ' ' +
    movies['actors'] + ' ' +
    movies['directors']
)

# Contoh cek data
print(movies[['title', 'features']].head(1))

# Model Development 
# Hitung Similarity Matrix & Fungsi Rekomendasi
# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(movies['features'])

# Hitung similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Fungsi rekomendasi dengan error handling
def get_recommendations(title, top_n=10):
  try:
    # Cari Index film
    idx = movies[movies['title'] == title].index[0]
    
    # Ambil similarity score
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Ambil top_n rekomendasi (exclude film itu sendiri)
    sim_indices = [i[0] for i in sim_scores[1:top_n+1]]
    
    # Return judul, genre, IMDb score, actors, directors dan similarity score
    recommendations = movies.iloc[sim_indices][['title', 'genres', 'imdb_score', 'actors', 'directors']]
    recommendations['similarity_score'] = [i[1] for i in sim_scores[1:top_n+1]]
    return recommendations

  except:
    return 'Film tidak ditemukan dalam database'

# evaluasi Model
# Contoh evaluasi rekomendasi untuk film 'The Platform'
recommendations = get_recommendations('The Platform', top_n=10)

# Hitung proporsi film niche (IMDb <= 7.0)
niche_movies = recommendations[recommendations['imdb_score'] <= 7.0]
niche_percentage = (len(niche_movies) / len(recommendations)) * 100
print(f'Proporsi Konten Niche: {niche_percentage:.2f}%')

# Cek kesamaan genre dengan film target
target_genres = movies[movies['title'] == 'The Platform']['genres'].iloc[0]
recommended_genres = recommendations['genres'].explode().value_counts()

print('\nGenre Rekomendasi:')
print(recommended_genres)

# Visualisasi hasil
# Plot similarity score
plt.figure(figsize=(10, 6))
sns.barplot(x=recommendations['similarity_score'], y=recommendations['title'], palette='mako')
plt.title('Similarity Score Rekomendasi untuk Film "The Platform"')
plt.xlabel('Similarity Score')
plt.ylabel('Judul Film')

# Cek kesamaan genre dengan film target
plt.figure(figsize=(10, 5))
sns.histplot(recommendations['imdb_score'], bins=20, kde=True)
plt.title('Distribusi IMDb Score Rekomendasi')

# uji Model
# Rekomendsi untuk 'The Dark Knight Rises'
rec = get_recommendations('The Dark Knight Rises', top_n=10)
print('\nRekomendasi untuk film yang mirip "The Dark Knight Rises": ')
print(rec[['title', 'genres', 'directors', 'actors', 'imdb_score']])

# Rekomendasi untuk film niche (contoh: "The Cloverfield Paradox")
cloverfield_rec = get_recommendations("The Cloverfield Paradox", top_n=5)
print("\nRekomendasi untuk Film Niche:")
print(cloverfield_rec[['title', 'imdb_score']])

# save Model
pickle.dump(tfidf, open('tfidf_model.pkl', 'wb'))
pickle.dump(cosine_sim, open('cosine_sim.pkl', 'wb'))
