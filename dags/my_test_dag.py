import requests
import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

default_args = {
    'params': {
        "rateDate": "latest"
    }
}

base = 'BTC'
symbol = 'USD'
dateformat = '%Y-%m-%d'

def retrieveRate(ti=None, params=None):
    url = f'https://api.exchangerate.host/{params["rateDate"]}?base={base}&symbols={symbol}'
    responce = requests.get(url).json()
    pair = f'{base}/{symbol}'
    curdate = responce["date"]
    rate = float(responce["rates"][symbol])
    ti.xcom_push(key='pair', value=pair)
    ti.xcom_push(key='curdate', value=curdate)
    ti.xcom_push(key='rate', value=rate)
    return

with DAG(
    dag_id='BTC_Rate_DAG',
    schedule_interval='0 */3 * * *',
    start_date=datetime.datetime(2021, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=['demo']
) as dag:
    create_out_table = PostgresOperator(
        task_id="create_out_table",
        postgres_conn_id="airflow_out",
        sql="sql/create_out_table.sql",
    )

    retrieve_rate = PythonOperator(
        task_id='retrieve_rate',
        provide_context=True,
        python_callable=retrieveRate,
    )

    insert_value = PostgresOperator (
        task_id='insert_value',
        postgres_conn_id="airflow_out",
        sql="sql/insert_value.sql",
    )

    create_out_table >> retrieve_rate >> insert_value