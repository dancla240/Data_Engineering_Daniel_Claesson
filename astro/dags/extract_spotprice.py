from airflow.models import DAG
from airflow.io.path import ObjectStoragePath
import pandas as pd
#from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import os

def get_datestring() -> str:
    tid = datetime.now()
    datestring = str(str(tid.year)+'/0'+str(tid.month)+'-'+str(tid.day)+'_SE3.json')
    return datestring

def get_spotprice(datestring):
    url = f'https://www.elprisetjustnu.se/api/v1/prices/{datestring}'
    req = requests.get(url=url)
    if (req):
        data = req.json()
        df = pd.DataFrame(data)
        path = ObjectStoragePath('s3://s3service:9010', conn_id="s3") #'object store path object'
        filename = f'spotpris_{datestring}.csv'
        full_path = path/filename
        with open(full_path, 'w', newline='') as file:
            df.to_csv(file)


with DAG(
    dag_id='retrieve_daily_spotprice',
    schedule_interval='@daily',
    start_date=datetime(2024, 6, 10)
) as dag:
    
    task_get_datestring = PythonOperator(
        task_id = 'get_datestring',
        python_callable = get_datestring,
    )

    task_get_spotprice = PythonOperator(
        task_id = 'get_spotprice',
        python_callable = get_spotprice,
    )

    task_get_datestring >> task_get_spotprice