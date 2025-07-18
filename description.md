# Judul Project
Project ini berjudul
Analisis Tren Penjualan Suplemen dan Multivitamin dengan Parameter Waktu Bulanan dan Sub Kategori di Setiap Item 
## Repository Outline
```
1. README.md - Penjelasan gambaran umum project
2. GX.ipynb - Notebook yang berisi analisa untuk memastikan data dengan great expectation dan mengetahui kualitas data
3. dag.py - menjelaskan tentang pengambilan data dari posgreSQL, melakukan cleaning data, dan mengunggah dalam elastichsearch
4. dag_graph.png - hasil screenshoot dari flow pengerjaan dag.py
5. conceptual.txt - Menjawab tentang pertanyaan yang disediakan
6. clean.csv - dataset yang sudah dilakukan cleaning
7. raw_data.csv - data set awal
8. ddl.txt - berisi url dari dataset, syntax untuk membuat table_3 di posgreSQL, import data ke cmd, import data ke postgreSQL
9. folder images - berisi screenshot data hasil plot dan analisanya
```

## Problem Background
Latar Belakang
Menurut https://www.kompas.id/baca/riset/2023/07/10/kesadaran-tentang-kesehatan-mental-mulai-tumbuh, Kesehatan sangat penting untuk diperhatikan. Sadarnya akan kesehatan di kehidupan saat ini sudah mulai membaik dan dipertimbangkan dengan rutin mengkonsumsi suplemen seperti protein, vitamin, omega, dan asam amino. Semakin sadarnya akan kesehatan, penjualan suplemen juga semakin meningkat sehingga harus adanya analisa penjualan lebih lanjut untuk menganalisa perkembangan dan persebaran bisnis mengenai suplemen kesehatan. Analisa ini bertujuan untuk perkembangan bisnis dan evaluasi bisnis agar mengetahui segmen apa yang harus dikembangkan dan segmen mana yang harus dievaluasi baik secara distribusi maupun segi promosi.

Tujuan
Saat ini, saya merupakan seorang Data Analyst di perusahaan farmasi. Report akan diberikan mengenai penjualan mingguan untuk produk suplemen berdasarkan kategori suplemen, lokasi cabang penjualan, serta menganalisa penjualan berdasarkan diskon yang tersedia sebelumnya. Tindak lanjut dari report ini bertujuan untuk mengevaluasi penjualan secara cabang, platform penjualan, maupun segmen barang yang dijual agar mengetahui hasil dari proses penjualan dan dapat mengevaluasi kekurangan dari produk yang diindikasikan kurang terdistribusi dengan baik.

Divisi/tim yang membutuhkan
Divisi Marketing dan Sales

## Project Output
Output berupa plot dan analisa data untuk analisa lebih lanjut di divisi marketing & sales

## Data
data diambil dari kaggle dengan jumlah 10 kolom dan 43850 data

## Method
project ini menggunakan system docker yang berisikan elasticsearch airflow dan kibana untuk visualisasi serta melakukan koneksi dengan posgresql untuk pembuatan tabel data

## Stacks
Library yang digunakan
import pandas as pd
import datetime as dt
from datetime import timedelta
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import psycopg2
from psycopg2 import sql, OperationalError
from elasticsearch import Elasticsearch, helpers
serta visualisasi di kibana dan pemanggulan data awal di postgreSQL

## Reference
- https://www.kaggle.com/datasets/zahidmughal2343/supplement-sales-data
- https://www.kompas.id/baca/riset/2023/07/10/kesadaran-tentang-kesehatan-mental-mulai-tumbuh
- https://www.elastic.co/kibana
- https://logz.io/blog/kibana-tutorial/
- https://www.digitalcommerce360.com/2025/02/06/ecommerce-trends-top-online-retailers-international-sales/
- https://en.wikipedia.org/wiki/2024_United_States_presidential_election
