# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = '/home/Assignment/01_data_pipeline/scripts/unit_test/'
DB_FILE_NAME = 'utils_output.db'
UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'
DATA_DIRECTORY = '/home/Assignment/01_data_pipeline/scripts/unit_test/'
INTERACTION_MAPPING = '/home/Assignment/01_data_pipeline/scripts/unit_test/interaction_mapping.csv'
INDEX_COLUMNS_INFERENCE = ['total_leads_droppped', 'city_tier', 'referred_lead', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'created_date']
INDEX_COLUMNS_TRAINING = ['total_leads_droppped', 'city_tier', 'referred_lead', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'app_complete_flag', 'created_date']
NOT_FEATURES = ['created_date', 'assistance_interaction', 'career_interaction', 'payment_interaction', 'social_interaction', 'syllabus_interaction']
index_variable=['created_date', 'first_platform_c','first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier','referred_lead', 'app_complete_flag']

