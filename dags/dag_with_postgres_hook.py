import csv
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

default_args = {
    'owner': 'luis',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

def postgres_to_s3():
    pass
    # Step 1: query data from postgresql db and save it into text file
    hook = PostgresHook(postgres_conn_id='postgres_localhost')
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from orders where date <= '20220501'")
    
    with open("dags/get_orders.txt", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        
    cursor.close()
    conn.close()
    
    logging.info("Saved orders data in text file get_orders.txt")
    
    # Step 2: upload the text file to S3

with DAG(
    dag_id='dag_with_postgres_hook_v01',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2025, 12, 20)
) as dag:
    task1 = PythonOperator(
        task_id='postgres_to_s3',
        python_callable=postgres_to_s3
    )
    task1