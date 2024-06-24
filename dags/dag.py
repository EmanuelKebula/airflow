from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def print_message():
    print("Questo è un messaggio di log.")

# Definizione del DAG
with DAG(
    dag_id='version1.0',
    start_date=datetime(year=2024, month=6, day=21, hour=14, minute=30),
    schedule_interval=timedelta(minutes=10),
    catchup=False
) as dag:
    # Definizione dei task
    start_task = PythonOperator(
        task_id='print_message',
        python_callable=print_message
    )

    end_task = EmptyOperator(
        task_id='end'
    )

    # Definizione della dipendenza tra i task
    start_task >> end_task
