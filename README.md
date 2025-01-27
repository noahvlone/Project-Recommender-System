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

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.
