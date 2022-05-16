import os
from zipfile import ZipFile
import json
import pandas as pd
import geohash2 as gh
import boto3

from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
COUNTRY = os.environ.get("COUNTRY")
BUCKET = os.environ.get("BUCKET")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")


def get_full_df(local_zip_path, filename):
    """
    Function to convert a csv file (inside a zip file) into a pandas dataframe
    :param local_zip_path: string of the zip file path
    :param filename: string with the csv file name inside the zip file
    :return: pandas dataframe
    """
    with ZipFile(local_zip_path) as zip_file:
        with zip_file.open(filename) as csv_file:
            output_dataframe = pd.read_csv(csv_file)
    return output_dataframe


def dataframe_transformation(**kwargs):  # pylint: disable=unused-argument)
    """

    :param kwargs:
    :return:
    """
    task_instance = kwargs['ti']
    dataframe = task_instance.xcom_pull(task_ids='convert_file_to_dataframe')
    # Filter dataframe by country
    # If there is no country to filter it will return all the dataset
    if COUNTRY is None:
        print('LOG: No country to filter. Returning all the World')
        output_dataframe = dataframe
    else:
        print(f'LOG: Getting cities from {COUNTRY}..')
        output_dataframe = dataframe[dataframe.country == COUNTRY]

    # Selecting columns
    print('LOG: Selecting columns...')
    argv = ['city', 'lat', 'lng', 'population']
    out_dataframe = pd.DataFrame()
    for arg in argv:
        out_dataframe[arg] = output_dataframe[[arg]]

    # Building extra column
    print('LOG: Adding GeoHash column...')
    out_dataframe["geohash"] = out_dataframe.apply(lambda x: gh.encode(x.lat, x.lng, precision=12)
                                                   , axis=1)
    return out_dataframe


def from_df_to_json(json_filename, **kwargs):  # pylint: disable=unused-argument)
    """
    Function to convert a pandas dataframe into a JSON file
    :param dataframe: pandas dataframe
    :param json_filename: string with the name necessary for the JSON file
    :return: None
    """
    task_instance = kwargs['ti']
    dataframe = task_instance.xcom_pull(task_ids='transform_dataframe')
    result = dataframe.to_json(orient="records")
    parsed = json.loads(result)
    with open(json_filename, 'w', encoding='utf-8') as file_open:
        json.dump(parsed, file_open, ensure_ascii=False, indent=4)


def upload_to_s3(s3_path, filename,):
    """
    Function to upload a file into AWS S3
    :param filename: string with the name of the file to upload
    :param s3_path: string with the name of a s3 path without the file name
    :return: None
    """
    region_name = 'eu-west-1'
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY
                             , aws_secret_access_key=AWS_SECRET_KEY
                             , region_name=region_name)
    try:
        s3_client.upload_file(filename, BUCKET, f'{s3_path}{filename}')
        print(f'LOG: The file {filename} was inserted in s3://{BUCKET}/{s3_path} with success !')
    except Exception as err:
        print(f"LOG: Some ERROR occur when inserting the file "
              f"{filename} in s3://{BUCKET}/{s3_path} "
              f"({err})")


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

    dataframe_transformation = PythonOperator(
        task_id=f'dataframe_transformation',
        python_callable=dataframe_transformation,
    )

    from_df_to_json = PythonOperator(
        task_id=f'convert_dataframe_in_{COUNTRY}_json',
        python_callable=from_df_to_json,
        op_kwargs={
            "json_filename": f'{COUNTRY}.json',
        }
    )
    upload_to_s3 = PythonOperator(
        task_id=f'upload_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={
            "filename": f'{COUNTRY}.json',
            "s3_path" : f'refined/{COUNTRY}/'
        }
    )

    download_dataset_task >> convert_file_to_dataframe >> dataframe_transformation
    dataframe_transformation >> from_df_to_json >> upload_to_s3
