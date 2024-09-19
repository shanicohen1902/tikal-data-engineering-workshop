# Data Engineering Course Exercises with Apache Airflow

## Installation

### Install with docker-compose
```sh
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env        
docker-compose up airflow-init
docker-compose up
```

### Standalone
```sh
AIRFLOW_HOME={folder}/dbt-workshop/apache_airflow
cd apache_airflow
airflow standalone
```