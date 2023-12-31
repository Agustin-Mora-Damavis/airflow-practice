from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import time


def _show_hello():
    time.sleep(20.0)
    print("Hello World!")


with DAG(
    "dummy_dag",
    start_date=datetime(2023, 6, 29),
    schedule_interval="@daily",
    catchup=False
) as dag:
    
    show_hello = PythonOperator(
        task_id="show_hello",
        python_callable=_show_hello
    )

    show_hello

