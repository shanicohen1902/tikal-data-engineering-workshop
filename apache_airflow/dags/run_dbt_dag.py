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

dag = DAG('dbt_run_exercise',
          default_args=default_args,
          schedule_interval='@once',
          tags=['dbt'])

echo_airflow_home = BashOperator(
    task_id='pwd',
    bash_command='echo $AIRFLOW_HOME',
    dag=dag
)

run_dbt = BashOperator(
    task_id='run_dbt',
    bash_command='cd $AIRFLOW_HOME/../dbt/cost_allocation && dbt run',
    dag=dag,
    outlets=[example_dataset]
)

echo_airflow_home >> run_dbt


###########
