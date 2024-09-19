from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 18),
    'retries': 0,
    'catchup': False
}

dag = DAG('dbt_run_exercise', default_args=default_args, schedule_interval='@once')

run_dbt = BashOperator(
    task_id='run_dbt',
    bash_command='cd /Users/shani.cohen/dev/dbt-workshop/cost_allocation/cost_allocation && dbt run',
    dag=dag,
)
