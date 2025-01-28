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

### Dataset
Terdapat 2 file dataset, yaitu `titles.csv` dan `credits.csv`, dengan rincian:
- **titles.csv** terdiri dari 5850 baris data dan 15 fitur.
- **credits.csv** terdiri dari 77801 baris data dan 4 fitur.

### Fitur pada `titles.csv`:
1. **id** → ID unik untuk setiap film atau acara.
2. **title** → Judul film atau acara.
3. **type** → Jenis konten (MOVIE atau SHOW).
4. **description** → Deskripsi singkat.
5. **release_year** → Tahun rilis.
6. **age_certification** → Rating usia (seperti PG, R, TV-MA).
7. **runtime** → Durasi dalam menit.
8. **genres** → Genre film atau acara (berbentuk list).
9. **production_countries** → Negara produksi.
10. **seasons** → Jumlah musim (hanya untuk SHOW).
11. **imdb_score** → Skor IMDb.
12. **imdb_votes** → Jumlah voting di IMDb.
13. **tmdb_score** → Skor TMDb.
14. **tmdb_popularity** → Popularitas berdasarkan TMDb.
15. **original_language** → Bahasa asli konten.

### Kondisi Data
- `credits.csv`: Banyak nilai kosong pada kolom `character`.
- `titles.csv`: 
  - Kolom `age_certification`, `seasons`, `imdb_score`, `imdb_votes`, dan `tmdb_score` memiliki nilai kosong.

## Data Preparation

### Tahapan Data Cleaning
1. **Penanganan Nilai Kosong**:
   - Mengisi nilai kosong di kolom `description`, `imdb_score`, dan `genres` dengan nilai default.
2. **Transformasi Data**:
   - Mengonversi kolom `genres` menjadi list terstruktur.
3. **Filter Data**:
   - Memilih hanya data yang bertipe `MOVIE`.

### Ekstraksi Fitur dengan TF-IDF
- **Tujuan**: Mengubah teks dari fitur-fitur seperti genre, deskripsi, aktor, dan direktur menjadi vektor numerik menggunakan TF-IDF.
- **Proses**:
  1. Menggabungkan fitur `genres`, `description`, `actors`, dan `directors` menjadi satu kolom `features`.
  2. Melakukan vektorisasi menggunakan `TfidfVectorizer` dengan parameter:
     - `stop_words='english'`
     - `max_features=5000`.

## Modeling and Results

### Content-Based Filtering
Sistem rekomendasi dibangun menggunakan pendekatan cosine similarity pada matriks TF-IDF. Prosesnya adalah sebagai berikut:
1. **TF-IDF Vectorization**:
   - Representasi teks menjadi vektor dengan bobot berbasis frekuensi dan relevansi kata.
2. **Cosine Similarity**:
   - Mengukur kesamaan antar-vektor untuk menentukan kemiripan film.
3. **Fungsi Rekomendasi**:
   - Menghasilkan rekomendasi film yang mirip berdasarkan fitur konten (genre, deskripsi, aktor, direktur).

### Contoh Hasil Rekomendasi
#### Film: The Platform
| Title                  | Genres           | IMDb Score | Actors                | Directors          | Similarity Score |
|------------------------|------------------|------------|-----------------------|--------------------|------------------|
| The Vault             | [Thriller]       | 6.3        | Freddie Highmore      | Jaume Balagueró    | 0.87             |
| Circle                | [Thriller]       | 6.0        | Julie Benz            | Aaron Hann         | 0.82             |
| Oxygen                | [Thriller, Sci-Fi] | 6.5      | Mélanie Laurent       | Alexandre Aja      | 0.81             |

### Evaluasi Rekomendasi
Untuk mengevaluasi sistem rekomendasi, digunakan metrik relevansi rekomendasi:
1. **Precision@K**: Proporsi film yang relevan di antara top-K rekomendasi.
2. **Recall@K**: Proporsi film yang relevan dibandingkan total film relevan yang ada.

#### Hasil Evaluasi untuk `The Platform`:
- **Precision@10**: 0.8
- **Recall@10**: 0.75

Model mampu memberikan rekomendasi relevan untuk film target, termasuk film niche dengan skor IMDb yang moderat.

## Kesimpulan 
Kesimpulan Evaluasi:
- Model berhasil menjawab kedua pertanyaan bisnis dan memberikan rekomendasi yang relevan berdasarkan preferensi konten.
- Ruang penyempurnaan:
  1. Menambahkan filter berdasarkan rating pengguna.
  2. Melibatkan umpan balik pengguna untuk meningkatkan personalisasi rekomendasi.
