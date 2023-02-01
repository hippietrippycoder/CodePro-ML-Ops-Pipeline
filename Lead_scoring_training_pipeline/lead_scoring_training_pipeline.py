##############################################################################
# Import necessary modules
# #############################################################################

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os
import importlib.util
import sqlite3
from sqlite3 import Error
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import importlib.util
import sys
from Lead_scoring_training_pipeline import *

###############################################################################
# Define default arguments and DAG
# ##############################################################################

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

utils = module_from_file("utils", "airflow/dags/Lead_scoring_training_pipeline/utils.py")


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022,7,30),
    'retries' : 1, 
    'retry_delay' : timedelta(seconds=5)
}


ML_training_dag = DAG(
                dag_id = 'Lead_scoring_training_pipeline',
                default_args = default_args,
                description = 'Training pipeline for Lead Scoring System',
                schedule_interval = '@monthly',
                catchup = False,
                tags=['training_pipeline']
)

###############################################################################
# Create a task for encode_features() function with task_id 'encoding_categorical_variables'
# ##############################################################################
encoding_categorical_variables=PythonOperator(task_id='encoding_features',python_callable= utils.encode_features, dag=ML_training_dag)
###############################################################################
# Create a task for get_trained_model() function with task_id 'training_model'
# ##############################################################################
training_model=PythonOperator(task_id='mode_training',python_callable= utils.get_trained_model,dag=ML_training_dag)
###############################################################################
# Define relations between tasks
# ##############################################################################
encoding_categorical_variables.set_downstream(training_model)
