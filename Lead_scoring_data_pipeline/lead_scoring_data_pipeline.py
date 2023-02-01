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
from Lead_scoring_data_pipeline.dags.constants_data_pipeline import *
from Lead_scoring_data_pipeline.dags.city_tier_mapping import *
from Lead_scoring_data_pipeline.dags.significant_categorical_level import *
from datetime import datetime, timedelta
import importlib.util
import sys


###############################################################################
# Define default arguments and DAG
# ##############################################################################


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

utils = module_from_file("utils", "/home/airflow/dags/Lead_scoring_data_pipeline/utils.py")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022,12,16),
    'retries' : 1, 
    'retry_delay' : timedelta(seconds=5),
    'provide_context': True,
    'depends_on_past': False
}


ML_data_cleaning_dag = DAG(
                dag_id = 'Lead_Scoring_Data_Engineering_Pipeline',
                default_args = default_args,
                description = 'DAG to run data pipeline for lead scoring',
                schedule_interval = '@daily',
                catchup = False,
                tags=['data_pipeline']
)

###############################################################################
# Create a task for build_dbs() function with task_id 'building_db'
# ##############################################################################
building_db=PythonOperator(task_id='building_dbs',python_callable= utils.build_dbs,op_kwargs={'db_path':DB_PATH, 'data_directory':LOAD_DATA_DIRECTORY,'start_date':start_date,'end_date':end_date}, dag=ML_data_cleaning_dag)
###############################################################################
# Create a task for raw_data_schema_check() function with task_id 'checking_raw_data_schema'
# ##############################################################################
checking_raw_data_schema=PythonOperator(task_id='raw_data_schema_check',python_callable= utils.raw_data_schema_check,dag=ML_data_cleaning_dag)
###############################################################################
# Create a task for load_data_into_db() function with task_id 'loading_data'
# #############################################################################
loading_data=PythonOperator(task_id='data_loader',python_callable= utils.load_data_into_db,dag=ML_data_cleaning_dag)
###############################################################################
# Create a task for map_city_tier() function with task_id 'mapping_city_tier'
# ##############################################################################
mapping_city_tier=PythonOperator(task_id='city_tier_mapping',python_callable= utils.map_city_tier,dag=ML_data_cleaning_dag)
###############################################################################
# Create a task for map_categorical_vars() function with task_id 'mapping_categorical_vars'
# ##############################################################################
mapping_categorical_vars=PythonOperator(task_id='catg_mapping',python_callable= utils.map_categorical_vars,dag=ML_data_cleaning_dag)
###############################################################################
# Create a task for interactions_mapping() function with task_id 'mapping_interactions'
# ##############################################################################
mapping_interactions=PythonOperator(task_id='inter_mapping',python_callable= utils.interactions_mapping,dag=ML_data_cleaning_dag)
###############################################################################
# Create a task for model_input_schema_check() function with task_id 'checking_model_inputs_schema'
# ##############################################################################
checking_model_inputs_schema=PythonOperator(task_id='modelschema_input_check',python_callable= utils.model_input_schema_check,dag=ML_data_cleaning_dag)
###############################################################################
# Define the relation between the tasks
building_db.set_downstream(checking_raw_data_schema)
checking_raw_data_schema.set_downstream(loading_data)
loading_data.set_downstream(mapping_city_tier)
mapping_city_tier.set_downstream(mapping_categorical_vars)
mapping_categorical_vars.set_downstream(mapping_interactions)
mapping_interactions.set_downstream(checking_model_inputs_schema)
# ##############################################################################


