# Laporan Proyek Machine Learning - Farhan Ramadhan

## Project Overview

Industri film dan media berkembang pesat dengan banyaknya konten yang tersedia di berbagai platform streaming. Pengguna sering kali kesulitan menemukan konten yang sesuai dengan preferensi mereka karena jumlah pilihan yang sangat besar. Oleh karena itu, sistem rekomendasi menjadi alat penting untuk membantu pengguna menemukan film yang relevan dengan preferensi mereka, baik itu film populer maupun konten niche.

  Format Referensi: [Kaggle](https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies) 

## Business Understanding

Dalam industri hiburan, pengguna sering kali merasa kesulitan menemukan film yang sesuai dengan preferensi mereka di tengah banyaknya pilihan yang tersedia. Permasalahan ini menjadi semakin kompleks karena adanya perbedaan preferensi pengguna, seperti sebagian ingin mencari film populer, sementara yang lain lebih menyukai konten unik atau niche. Oleh karena itu, diperlukan sebuah sistem rekomendasi yang dapat membantu pengguna menemukan film dengan relevansi tinggi berdasarkan fitur seperti genre, deskripsi, aktor, dan direktor, serta memberikan rekomendasi yang memenuhi kebutuhan berbagai segmen pengguna.

### Problem Statements

Menjelaskan pernyataan masalah:
- Pernyataan Masalah 1: Bagaimana cara merekomendasikan film yang relevan berdasarkan film tertentu yang dipilih oleh pengguna?
- Pernyataan Masalah 2: Apakah sistem dapat memberikan rekomendasi film niche untuk pengguna yang menyukai konten unik atau kurang populer?

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Jawaban pernyataan masalah 1: Membangun sistem rekomendasi berbasis konten (Content-Based Filtering) untuk membantu pengguna menemukan film berdasarkan kesamaan fitur seperti genre, deskripsi, aktor, dan direktur.
- Jawaban pernyataan masalah 2: Memberikan rekomendasi film niche untuk pengguna yang menginginkan konten yang tidak terlalu populer.

## Data Understanding
terdapat 2 file dataset yaitu titles.csv dan credits.csv yang terdiri dari: 5850 baris data dan 77801 baris data. [Kaggle](https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies).

Kondisi Data, Missing Value:
- character di credits.csv memiliki banyak nilai kosong.
- age_certification dan seasons di titles.csv memiliki banyak nilai kosong.
- imdb_score, imdb_votes, dan tmdb_score memiliki sebagian data kosong.
- Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

Variabel-variabel pada dataset adalah sebagai berikut:

Kolom-kolom utama pada credits.csv:
- person_id → ID unik untuk setiap orang.
- id → ID film atau acara (berhubungan dengan titles.csv).
- name → Nama aktor atau kru.
- character → Nama karakter yang dimainkan (banyak nilai kosong).
- role → Peran dalam produksi (misalnya, ACTOR, DIRECTOR).

Kolom-kolom utama:
- id → ID film atau acara (berhubungan dengan credits.csv).
- title → Judul film atau acara.
- type → Jenis konten (MOVIE atau SHOW).
- description → Deskripsi singkat.
- release_year → Tahun rilis.
- age_certification → Rating usia (seperti PG, R, TV-MA).
- runtime → Durasi dalam menit.
- genres → Genre film atau acara (berbentuk list).
- production_countries → Negara produksi.
- seasons → Jumlah musim (hanya untuk SHOW).
- imdb_score → Skor IMDb.
- tmdb_score → Skor TMDb.
- tmdb_popularity → Popularitas berdasarkan TMDb.

**Exploratory Data Analysis**:
![Image](https://github.com/user-attachments/assets/ed132d0c-6842-43be-9eab-14543cdebd75)
- Insight:
  1. Genre drama adalah yang paling banyak muncul, diikuti oleh komedi. Hal ini mencerminkan bahwa industri film lebih banyak memproduksi film bergenre naratif emosional dan humor, kemungkinan karena permintaan pasar yang tinggi untuk hiburan yang relatable dan ringan. Thriller dan Action di Posisi Selanjutnya
  2. Thriller dan action juga memiliki jumlah yang signifikan. Hal ini menunjukkan bahwa film yang penuh ketegangan dan aksi banyak diproduksi, kemungkinan karena daya tariknya terhadap audiens global, terutama dalam industri Hollywood dan film blockbuster. Romance dan Dokumenter Juga Cukup Populer
  3. Film romance dan documentation memiliki jumlah yang lumayan besar, menunjukkan bahwa kisah percintaan dan dokumenter memiliki basis penonton yang stabil. Dokumenter yang berkembang bisa jadi mencerminkan peningkatan minat terhadap edukasi dan realita sosial dalam bentuk audiovisual. Genre Niche dengan Jumlah Lebih Sedikit
  4. Genre seperti western, war, sport, dan reality memiliki jumlah yang sangat sedikit. Ini menunjukkan bahwa genre tersebut memiliki audiens yang lebih terbatas atau kurang populer di pasar global.

![Image](https://github.com/user-attachments/assets/b4429e86-eea7-4bf1-b173-297495132832)
- Insight: Berdasarkan hasil diatas dapat dijelaskan bahwa film The Platform memiliki kesamaan dengan film The Vault. kesamaan ini berasal dari genre, imdb score, dan actor.
  
![Image](https://github.com/user-attachments/assets/57f00ff9-2700-43dc-8db0-9712753c05d4)
- Insight: Mayoritas Skor di Kisaran 5.5 – 6.5: Sebagian besar film yang direkomendasikan memiliki skor di sekitar 5.5 hingga 6.5, yang umumnya dikategorikan sebagai film dengan kualitas rata-rata hingga cukup baik. Hal ini menunjukkan bahwa sistem rekomendasi cenderung mengusulkan film dengan skor yang relatif sedang, bukan yang sangat tinggi atau sangat rendah.

## Data Preparation
- menghapus missing value menggunakan fungsi fillna()
- menggabungkan beberapa fitur seperti: judul, genre, aktor, direktor untuk modeling
- menghitung similarity matrix menggunakan Tfidf Vectorization

**tahap yang dilakukan dalam notebook**: 
Text Preprocessing:
1. Mengubah data kompleks (list) menjadi format teks siap olah.
2. Penanganan missing value (fillna).

Feature Engineering:
1. Menggabungkan fitur-fitur terpisah menjadi satu fitur teks (bag of words).
   Teknik ini umum digunakan untuk:
   - Sistem rekomendasi berbasis konten (content-based filtering).
   - Pemrosesan NLP seperti TF-IDF atau model vektor teks.

String Manipulation:
1. Penggabungan string (+), join(), dan konversi tipe data (astype).

## Modeling
Algoritma yang digunakan adalah Content-Based Filtering dengan pendekatan TF-IDF Vectorization dan Cosine Similarity. Ini adalah sistem rekomendasi yang merekomendasikan item berdasarkan kemiripan fitur konten item tersebut.

cara kerja: Cara Kerja Program
1. TF-IDF Vectorization:

tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(movies['features'])

 - Tujuan: Mengubah teks di kolom features menjadi representasi numerik (vektor) agar bisa dihitung kemiripannya.

 - Proses:
TF-IDF (Term Frequency-Inverse Document Frequency):

 - Menghitung bobot kata dengan memperhatikan:
   - Term Frequency (TF): Frekuensi kata dalam satu dokumen (film).
   - Inverse Document Frequency (IDF): Menurunkan bobot kata yang umum muncul di banyak dokumen.
   - Contoh: Kata "action" yang sering muncul di satu film tetapi jarang di film lain akan memiliki bobot tinggi.

- Parameter:
  
  1. stop_words='english': Menghapus kata umum (seperti "the", "and") yang tidak informatif.
  2. max_features=5000: Membatasi fitur ke 5000 kata paling signifikan untuk mengurangi dimensi data.

2. Cosine Similarity:
   
   - cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
   - Tujuan: Menghitung kemiripan antar film berdasarkan vektor TF-IDF.

- Proses:
  - Cosine Similarity: Mengukur sudut antara dua vektor.
  - Rentang nilai: 0 (tidak mirip) hingga 1 (sangat mirip).
  - Contoh: Jika film A dan B memiliki vektor yang searah (sudut 0°), skor = 1.

3. Fungsi Rekomendasi

 - def get_recommendations(title, top_n=10):
      ... (lihat kode lengkap di pertanyaan)
    
 - Tujuan: Mencari film-film paling mirip dengan film input.

 - Proses:
   - Mencari indeks film yang ingin direkomendasikan.
   - Mengambil skor kemiripan dari matriks cosine_sim untuk film tersebut.
   - Mengurutkan skor kemiripan dari tertinggi ke terendah.
   - Memilih indeks film dengan skor tertinggi (kecuali film itu sendiri).
   - Menampilkan informasi film rekomendasi beserta skor kemiripan.

Kelebihan Metode Ini:
1. Tidak Membutuhkan Data Pengguna: Hanya menggunakan fitur item (film) untuk rekomendasi, cocok untuk cold-start problem (kasus ketika data pengguna belum ada).

2. Transparan dan Interpretabel: Rekomendasi berdasarkan fitur yang jelas (genre, aktor, deskripsi), sehingga mudah dipahami alasan rekomendasinya.

3. Efisien untuk Dataset Kecil-Sedang: Perhitungan TF-IDF dan cosine similarity relatif cepat untuk dataset dengan ukuran moderat.

4. Personalisasi Sederhana: Jika pengguna menyukai suatu film, sistem akan merekomendasikan film dengan konten serupa.

Kekurangan Metode Ini:
1. Keterbatasan pada Fitur Tersembunyi: Tidak bisa menangani preferensi kompleks pengguna yang tidak tercermin dalam fitur yang ada (misalnya tren atau konteks sosial).

2. Masalah Sparsitas: Jika fitur teks terlalu sedikit atau tidak informatif, TF-IDF tidak bisa menangkap kemiripan dengan baik.

3. Over-Specialization: Cenderung merekomendasikan item yang terlalu mirip, sehingga mengurangi kejutan (serendipity) bagi pengguna.

4. Skalabilitas: Perhitungan cosine similarity untuk dataset besar (misal jutaan item) akan sangat memakan sumber daya.


## Evaluation
1. Evaluasi I, Model menggunakan teknik Content-Based Filtering dengan matriks kesamaan berbasis TF-IDF. Dari hasil evaluasi:
   - Rekomendasi untuk film populer seperti "The Dark Knight Rises" menghasilkan daftar film yang relevan, dengan kesamaan pada genre, aktor, dan direktur.
   - Visualisasi skor kesamaan menunjukkan model berhasil mengidentifikasi film-film dengan kesamaan fitur.
   - Namun, analisis distribusi IMDb score rekomendasi mengungkapkan bahwa proporsi konten niche masih signifikan, yang berarti model tidak hanya merekomendasikan film dengan rating tinggi, tetapi juga niche.
     
Hasil ini menunjukkan model mampu menjawab pertanyaan bisnis pertama, dengan hasil relevan dan bervariasi sesuai konteks film yang dipilih.

2. Evaluasi II
   - Model diuji dengan contoh film niche seperti "The Cloverfield Paradox". Rekomendasi yang dihasilkan mencakup film dengan kesamaan tema dan genre, meskipun ratingnya bervariasi.
   - Model menunjukkan kemampuan mendeteksi film-film niche berdasarkan deskripsi, aktor, dan genre, dengan niche percentage dihitung sebagai indikator keberhasilan.
     
Model memenuhi tujuan ini dengan memberikan rekomendasi yang relevan dan mencakup konten niche, sehingga dapat memperluas jangkauan rekomendasi untuk pengguna.

## Kesimpulan 
Kesimpulan Evaluasi:
- Model yang dikembangkan berhasil menjawab kedua pertanyaan bisnis dan memenuhi tujuan. Namun, terdapat ruang untuk penyempurnaan, seperti:
  1. Menambahkan filter untuk pengguna yang hanya ingin melihat rekomendasi berdasarkan rating tertentu.
  2. Melibatkan umpan balik pengguna untuk meningkatkan personalisasi rekomendasi.
