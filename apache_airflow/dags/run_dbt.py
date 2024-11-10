from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator
from datetime import datetime

example_dataset = Dataset("s3://dataset/example.csv")

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
    outlets=[example_dataset]
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='cd /Users/shani.cohen/dev/dbt-workshop/cost_allocation/cost_allocation && dbt run',
    dag=dag,
)

run_dbt >> dbt_test


###########


dag = DAG('dbt_test_exercise', default_args=default_args, schedule=[example_dataset])

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='cd /Users/shani.cohen/dev/dbt-workshop/cost_allocation/cost_allocation && dbt run',
    dag=dag,
)

dbt_test
