# E-commerce, Multivitamin Sales

## Deskripsi Proyek
Proyek ini bertujuan sebagai laporan mingguan penjualan produk suplemen kesehatan berdasarkan kategori produk, lokasi cabang penjualan, dan analisa penjualan terkait diskon. Laporan ini ditujukan untuk Divisi Marketing dan Sales guna mengevaluasi performa penjualan cabang, platform distribusi, dan segmen produk yang kurang terdistribusi, untuk memperbaiki strategi penjualan dan distribusi produk.

## Pengguna/Penerima Output
- Divisi Marketing dan Sales

## Output
- Analisis data serta visualisasi dalam bentuk plot untuk evaluasi lebih lanjut oleh divisi marketing & sales.
- Insight penjualan mingguan berdasarkan kategori suplemen, lokasi cabang, dan evaluasi diskon.

## Teknologi dan Library yang Digunakan
- **Docker**: Sistem terpadu yang menjalankan Elasticsearch, Airflow, dan Kibana.
- **Database**: PostgreSQL untuk penyimpanan dan pembuatan tabel data awal.
- **Library Python**:
  - `pandas`, `datetime`, `timedelta` untuk manipulasi dan pengelolaan data waktu.
  - `sqlalchemy` dan `psycopg2` untuk koneksi dan operasi pada database PostgreSQL.
  - `airflow` dan `PythonOperator` untuk pengelolaan workflow otomatis.
  - `elasticsearch` dan `helpers` untuk indexing dan pencarian data.
- **Visualisasi**: Kibana untuk dashboard visualisasi data interaktif.

## Ringkasan Temuan
- **Pendapatan per Negara**:  
  - Kanada memiliki pendapatan tertinggi sekitar $31,394,319 dengan diskon rata-rata 12.5%.  
  - UK menyusul dengan pendapatan sekitar $30,815,841 pada diskon rata-rata 12.4%.  
  - USA memiliki pendapatan terendah sekitar $29,442,962 dengan diskon rata-rata 12.5%.  
- **Dampak COVID-19 pada Penjualan**:  
  - Pada masa pandemi, terjadi peningkatan signifikan pada segmen seperti Vitamin (+30-40%) dan Sleep Aid (+25%) karena kebutuhan kesehatan dan gangguan tidur selama lockdown.  
  - Segmen Performance dan Protein mengalami penurunan penjualan selama pandemi.  
  - Setelah pandemi, terjadi normalisasi penjualan dengan beberapa segmen seperti Sleep Aid tetap mengalami peningkatan.  
- **Analisa Diskon**  
  Diskon di ketiga negara cenderung stabil dan tidak menjadi faktor utama pendapatan; volume penjualan dan harga produk lebih dominan.  
- **Rekomendasi Strategi**  
  - USA perlu strategi baru untuk meningkatkan pendapatannya, mengingat potensi pasar yang besar.  
  - Fokus pada peningkatan distribusi dan promosi produk yang stagnan atau menurun seperti Fat Burner dan Amino Acid.  
  - Kemungkinan menggabungkan diskon produk terkait (misal Protein + Hydration, Omega + Herbal) untuk meningkatkan penjualan.

## Cara Penggunaan
1. Jalankan sistem terpadu menggunakan Docker yang mencakup Elasticsearch, Airflow, dan Kibana.  
2. Siapkan database PostgreSQL dan buat tabel data sesuai dengan kebutuhan proyek.  
3. Gunakan skrip Python ETL untuk ekstraksi, transformasi, dan pemuatan data ke PostgreSQL dan Elasticsearch.  
4. Jalankan DAG Airflow untuk otomatisasi pipeline data dan refresh visualisasi di Kibana.  
5. Akses dashboard Kibana untuk melihat hasil visualisasi dan analisa penjualan.

