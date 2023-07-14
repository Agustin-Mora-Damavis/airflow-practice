from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

from datetime import datetime


with DAG(
    "dummy_dag",
    start_date=datetime(2023, 6, 29),
    schedule_interval="@daily",
    catchup=False
) as dag:
    
    kubernetes_pod_operator = KubernetesPodOperator(
        name="kubernetes_pod_operator",
        pod_template_file="./spark-job.yaml"
    )
    
    kubernetes_pod_operator

