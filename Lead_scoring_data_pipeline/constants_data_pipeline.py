# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = '/home/airflow/dags/Lead_scoring_data_pipeline/'
DB_FILE_NAME = 'lead_scoring_data_cleaning.db'
UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'
DATA_DIRECTORY = '/home/airflow/dags/Lead_scoring_data_pipeline/'
LOAD_DATA_DIRECTORY = '/home/airflow/dags/Lead_scoring_data_pipeline/data/'
INTERACTION_MAPPING = '/home/airflow/dags/Lead_scoring_data_pipeline/mapping/interaction_mapping.csv'
INDEX_COLUMNS_INFERENCE = ['total_leads_droppped', 'city_tier', 'referred_lead', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'created_date']
INDEX_COLUMNS_TRAINING = ['total_leads_droppped', 'city_tier', 'referred_lead', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'app_complete_flag', 'created_date']
NOT_FEATURES = ['created_date', 'assistance_interaction', 'career_interaction', 'payment_interaction', 'social_interaction', 'syllabus_interaction']
start_date = '2022-12-15'
end_date = '2022-12-21'
index_variable=['created_date', 'first_platform_c','first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier','referred_lead', 'app_complete_flag']

