# Data Engineering Course Exercises with dbt and airflow

## part 1
[dbt workshop - exercises](dbt/readme.md)
[dbt workshop - slides](DBT.pdf)

## part 2
[airflow workshop](apache_airflow/readme.md)

## Requirements
### python virtual environment
```sh
pip install virtualenv
python -m venv env
source env/bin/activate
```

### Install DBT core
```sh
python -m pip install dbt-core
```

### Install DBT for DuckDB
```sh
python -m pip install  dbt-duckdb
```

### Install DuckDB
```sh
brew install duckdb # or something else for linux
```

## Airflow installation - standalone or docker  
### Airflow Standalone installation
```sh
export AIRFLOW_HOME={your_project_path}/dbt-workshop/apache_airflow
```
### Airflow Standalone execution
```
cd apache_airflow
airflow standalone
```

### Airflow Install with docker-compose (advanced)
```sh
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```
### Airflow docker-compose execution
```        
docker-compose up airflow-init #first-time
docker-compose up
```