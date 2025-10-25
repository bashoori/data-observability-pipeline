from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from scripts.fetch_api_data import fetch_data
from scripts.transform_data import transform_data
from scripts.load_to_sqlite import load_to_sqlite

default_args = {
    'owner': 'bita',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
}

with DAG(
    dag_id='api_to_sqlite_pipeline',
    default_args=default_args,
    description='Extract data from API and load into SQLite for analytics',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False
) as dag:

    extract = PythonOperator(task_id='fetch_api_data', python_callable=fetch_data)
    transform = PythonOperator(task_id='transform_data', python_callable=transform_data)
    load = PythonOperator(task_id='load_to_sqlite', python_callable=load_to_sqlite)

    extract >> transform >> load
