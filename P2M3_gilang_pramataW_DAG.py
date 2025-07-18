'''
=================================================
Milestone 3

Nama  : Gilang Pramata Wardhana
Batch : FTDS-043-RMT

Program ini dibuat untuk melakukan analisa data mengenai bisnis suplemen.  Semakin sadarnya akan Kesehatan, penjualan suplemen juga semakin meningkat sehingga harus adanya Analisa penjualan lebih lanjut untuk menganalisa perkembangan dan persebaran bisnis mengenai suplemen Kesehatan. Report ini bertujuan untuk menganalisa laporan penjualan mingguan untuk produk suplemen berdasarkan kategori suplemen, lokasi cabang penjualan, serta menganalisa penjualan berdasarkan berdasarkan diskon yang tersedia sebelumnya
Pada notebook ini, dijelaskan bahwa sedang melakukan proses pengambilan data dari postgresql kedalam server docker, lalu melakukan cleaning data di airflow dan melakukan upload ke elasticsearch
=================================================
'''


import pandas as pd
import datetime as dt
from datetime import timedelta
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import psycopg2
from psycopg2 import sql, OperationalError
from elasticsearch import Elasticsearch, helpers

"""
Pipeline ini mengekstrak data dari PostgreSQL, melakukan pembersihan, dan mengunggahnya ke Elasticsearch.
Digunakan untuk analisa tren penjualan produk kesehatan periode 2020-2025.

Komponen Utama:
1. Ekstrak data PostgreSQL
2. Cleaning data
3. Pengiriman data ke Elasticsearch untuk visualisasi ke Kibana

Jadwal Eksekusi:
Penjadwalan setiap sabtu jam 09:10, 09:20, 09:30 WIB
"""


default_args = {
    'owner': 'gilang',
    'start_date': dt.datetime(2024, 11, 1, 9, 10, 0) - timedelta(hours=7),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Menyesuaikan dbname, user, password, host, dan port sesuai dengan container docker
DB_CONFIG = {
    'dbname': 'airflow',
    'user': 'airflow',
    'password': 'airflow',
    'host': 'postgres', 
    'port': 5432,           # karena dari sql to airflow
}

RAW_CSV_PATH = '/opt/airflow/dags/table_m3.csv'
CLEAN_CSV_PATH = '/opt/airflow/dags/P2M3_gilang_pramataW_data_clean.csv'
ES_HOST = "http://elasticsearch:9200"

def export_data_from_postgres():
    """
    Mengekstrak data dari PostgreSQL ke file CSV
    1. Membuka koneksi ke database
    2. Mengeksekusi query SELECT *
    3. Menyimpan hasil ke .CSV
    """

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            query = sql.SQL("SELECT * FROM public.table_m3")
            df = pd.read_sql(query, conn)
        df.to_csv(RAW_CSV_PATH, index=False)
        print(f"Data exported to {RAW_CSV_PATH}")
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        raise

def clean_data():
    """
    Pembersihan data dan merapikan nama tabel
    1. Menghapus duplikat
    2. Standarisasi nama kolom (lowercase, remove spesi)
    3. Konversi format tanggal
    4. Handle missing values
    """

    df = pd.read_csv(RAW_CSV_PATH)
    df = df.drop_duplicates()

    df.columns = (
        df.columns.str.lower()
                  .str.replace(' ', '_', regex=False)
                  .str.replace(r'\s+', '', regex=True)
                  .str.replace(r'[^\w]', '', regex=True)
                  .str.strip()
    )

    for col in df.columns:
        if df[col].dtype == 'O':  # object/string
            df[col].fillna('', inplace=True)
        else:
            df[col].fillna(0, inplace=True)

    df.to_csv(CLEAN_CSV_PATH, index=False)
    print(f"Cleaned data saved to {CLEAN_CSV_PATH}")

def post_to_elasticsearch():
    """
    Mengunggah hasil cleaning data ke elasticsearch
    1. Membuat index
    2. Bulk insert data menggunakan helpers
    """

    es = Elasticsearch(ES_HOST)
    index_name = "table_m3_clean_data"

    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)

    df = pd.read_csv(CLEAN_CSV_PATH)

    actions = [
        {
            "_index": index_name,
            "_source": row.to_dict()
        }
        for _, row in df.iterrows()
    ]

    helpers.bulk(es, actions)
    print(f"Posted data to Elasticsearch index '{index_name}'")

with DAG(
    'P2M3_gilang_pramataW_DAG',
    default_args=default_args,
    description='DAG export data table_m3, clean, dan post ke Elasticsearch',
    schedule_interval='10,20,30 9 * * 6',  # Melakuakn penjadwalan di tiap sabtu jam 09:10, 09:20, 09:30 WIB
    catchup=False
) as dag:

    task_export = PythonOperator(
        task_id='export_data_from_postgres',
        python_callable=export_data_from_postgres,
    )

    task_clean = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
    )

    task_post_es = PythonOperator(
        task_id='post_to_elasticsearch',
        python_callable=post_to_elasticsearch,
    )

    task_export >> task_clean >> task_post_es
