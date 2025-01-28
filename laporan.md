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

Kolom-kolom utama pada credits.csv:
1. **person_id** → ID unik untuk setiap orang.
2. **id** → ID film atau acara (berhubungan dengan titles.csv).
3. **name** → Nama aktor atau kru.
4. **character** → Nama karakter yang dimainkan (banyak nilai kosong).
5. **role** → Peran dalam produksi (misalnya, ACTOR, DIRECTOR).
### Kondisi Data
- `credits.csv`: Banyak nilai kosong pada kolom `character`.
- `titles.csv`: 
  - Kolom `age_certification`, `seasons`, `imdb_score`, `imdb_votes`, dan `tmdb_score` memiliki nilai kosong.

## Exploratory Data Analysis
Distribusi Genre Film:
![Image](https://github.com/user-attachments/assets/ed132d0c-6842-43be-9eab-14543cdebd75)
- Insight:
  1. Genre drama adalah yang paling banyak muncul, diikuti oleh komedi. Hal ini mencerminkan bahwa industri film lebih banyak memproduksi film bergenre naratif emosional dan humor, kemungkinan karena permintaan pasar yang tinggi untuk hiburan yang relatable dan ringan. Thriller dan Action di Posisi Selanjutnya
  2. Thriller dan action juga memiliki jumlah yang signifikan. Hal ini menunjukkan bahwa film yang penuh ketegangan dan aksi banyak diproduksi, kemungkinan karena daya tariknya terhadap audiens global, terutama dalam industri Hollywood dan film blockbuster. Romance dan Dokumenter Juga Cukup Populer
  3. Film romance dan documentation memiliki jumlah yang lumayan besar, menunjukkan bahwa kisah percintaan dan dokumenter memiliki basis penonton yang stabil. Dokumenter yang berkembang bisa jadi mencerminkan peningkatan minat terhadap edukasi dan realita sosial dalam bentuk audiovisual. Genre Niche dengan Jumlah Lebih Sedikit
  4. Genre seperti western, war, sport, dan reality memiliki jumlah yang sangat sedikit. Ini menunjukkan bahwa genre tersebut memiliki audiens yang lebih terbatas atau kurang populer di pasar global.

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

### Hasil Rekomendasi
#### Hasil Rekomendasi untuk 'Naruto Shippuden the Movie':
|      | title                                               | genres                                                             |   imdb_score | directors          |   similarity_score |
|-----:|:----------------------------------------------------|:-------------------------------------------------------------------|-------------:|:-------------------|-------------------:|
|  322 | Naruto Shippuden the Movie: The Lost Tower          | ['animation', 'action', 'fantasy']                                 |          6.8 | Masahiko Murata    |           0.388594 |
|  330 | Naruto Shippuden the Movie: The Will of Fire        | ['action', 'comedy', 'drama', 'fantasy', 'animation']              |          7   | Masahiko Murata    |           0.354237 |
|  537 | Naruto Shippuden the Movie: Blood Prison            | ['action', 'comedy', 'horror', 'thriller', 'animation', 'fantasy'] |          7.1 | Masahiko Murata    |           0.34708  |
|  374 | Naruto: Legend of the Stone of Gelel                | ['fantasy', 'action', 'comedy', 'drama', 'animation']              |          6.4 | Hirotsugu Kawasaki |           0.341813 |
|  327 | Naruto Shippuden the Movie: Bonds                   | ['fantasy', 'animation', 'action']                                 |          6.8 | Hajime Kamegaki    |           0.319265 |
|  350 | Naruto: Ninja Clash in the Land of Snow             | ['comedy', 'fantasy', 'animation', 'action']                       |          6.6 | Tensai Okamura     |           0.298041 |
|  358 | Naruto: Guardians of the Crescent Moon Kingdom      | ['action', 'animation']                                            |          6.4 | Toshiyuki Tsuru    |           0.259924 |
| 3418 | The Seven Deadly Sins: Cursed by Light              | ['animation', 'fantasy', 'action']                                 |          6.4 | Takayuki Hamana    |           0.212997 |
|  304 | Inuyasha the Movie: Affections Touching Across Time | ['action', 'animation', 'fantasy']                                 |          7.2 | Toshiya Shinohara  |           0.157084 |
|  386 | Inuyasha the Movie 3: Swords of an Honorable Ruler  | ['animation', 'fantasy', 'action', 'thriller']                     |          7.6 | Toshiya Shinohara  |           0.142428 |

### Evaluasi Rekomendasi
Untuk mengevaluasi sistem rekomendasi, digunakan metrik relevansi rekomendasi:
1. **Precision@K**: Proporsi film yang relevan di antara top-K rekomendasi.
2. **Recall@K**: Proporsi film yang relevan dibandingkan total film relevan yang ada.

#### Hasil Evaluasi untuk `Naruto Shippuden the Movie`:
- **Precision@10**: 1.0
- **Recall@10**: 2.50

Model mampu memberikan rekomendasi relevan untuk film target, termasuk film niche dengan skor IMDb yang moderat.

## Kesimpulan 
Kesimpulan Evaluasi:
- Model berhasil menjawab kedua pertanyaan bisnis dan memberikan rekomendasi yang relevan berdasarkan preferensi konten.
- Ruang penyempurnaan:
  1. Menambahkan filter berdasarkan rating pengguna.
  2. Melibatkan umpan balik pengguna untuk meningkatkan personalisasi rekomendasi.
