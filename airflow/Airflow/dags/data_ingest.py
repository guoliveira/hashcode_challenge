import os
from zipfile import ZipFile
import pandas as pd

from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
COUNTRY = os.environ.get("COUNTRY")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")


def get_full_df(local_zip_path, filename):
    """

    :param local_zip_path:
    :param filename:
    :return:
    """
    with ZipFile(local_zip_path) as zip_file:
        df = pd.read_csv(zip_file.open(filename))
    return df


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id=f"Ingest_cities_from_{COUNTRY}",
    schedule_interval=None,
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['OLX'],
    start_date=datetime(2019, 1, 1)
) as dag:

    dataset_file = 'worldcities.zip'
    dataset_url = f"https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip"
    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f"curl -sSLf {dataset_url} > {path_to_local_home}/{dataset_file}"
    )

    convert_file_to_dataframe = PythonOperator(
        task_id=f'convert_file_to_dataframe',
        python_callable=get_full_df,
        op_kwargs={
            "local_zip_path": f'{path_to_local_home}/{dataset_file}',
            "filename": f'{path_to_local_home}/{dataset_file.replace(".zip",".csv")}'}
    )

    download_dataset_task >> convert_file_to_dataframe
