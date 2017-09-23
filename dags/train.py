# -*- coding:utf-8 -*-
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta,datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
default_args = {
            'owner': 'qiwei',
            'depends_on_past': False,
            'start_date': datetime(2017,9,23),
            'email': ['qqwei1123@163.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
             }

#-------------------------------------------------------------------------------
# dag

dag = DAG('train_dag',
           default_args=default_args,
           description='my first DAG',
           schedule_interval='*/3 * * * *')

train_operator = BashOperator(
            task_id='train_task',
            bash_command='/home/qiwei/workspace/ETL/Trains.py',
            dag=dag)
