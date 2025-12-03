from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'luis',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id="dag_with_catchup_backfill_v02",
    default_args=default_args,
    start_date=datetime(2025, 11, 25),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo This is a simple bash command."
    )
    
#run in terminal this command to backfill
#docker exec -it airflow_docker-airflow-webserver-1 airflow dags backfill dag_with_catchup_backfill_v02 --start-date 2025-11-26 --end-date 2025-12-02