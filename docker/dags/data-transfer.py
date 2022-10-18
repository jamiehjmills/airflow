import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime.date,
}

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='myapp.log',
                    filemode='w')

def test(*args, **kwargs):
    logging.info("this dag is now working")


with DAG(dag_id="data-transfer")\
        as dag:

    test = PythonOperator(
        task_id="test",
        python_callable=test
    )

