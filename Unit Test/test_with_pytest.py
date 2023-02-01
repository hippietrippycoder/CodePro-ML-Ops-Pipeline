##############################################################################
# Import the necessary modules
# #############################################################################
import pandas as pd
import os
import sqlite3
from sqlite3 import Error
from constants import *
from city_tier_mapping import *
from significant_categorical_level import *
from utils import *
print(DB_PATH)



###############################################################################
# Write test cases for load_data_into_db() function
# ##############################################################################

def test_load_data_into_db():
    """_summary_
    This function checks if the load_data_into_db function is working properly by
    comparing its output with test cases provided in the db in a table named
    'loaded_data_test_case'


    SAMPLE USAGE
        output=test_get_data()

    """
    load_data_into_db()
    
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    loaded_data= pd.read_sql('select * from loaded_data', cnx)
    
    cnx_ut= sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    test_case=pd.read_sql('select * from loaded_data_test_case', cnx_ut)
    
    def assertEquals(loaded_data, test_case):
        if loaded_data == test_case:
            return True
        else:
            return False
        
    cnx.close()
    cnx_ut.close()
    
    

""
test_load_data_into_db()


###############################################################################
# Write test cases for map_city_tier() function
# ##############################################################################
def test_map_city_tier():
    """_summary_
    This function checks if map_city_tier function is working properly by
    comparing its output with test cases provided in the db in a table named
    'city_tier_mapped_test_case'


    SAMPLE USAGE
        output=test_map_city_tier()

    """
    map_city_tier()
    
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    city_tier_mapped_df= pd.read_sql('select * from city_tier_mapped',cnx)
    
    cnx_ut= sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    test_case=pd.read_sql('select * from city_tier_mapped_test_case', cnx_ut)
    
    cnx.close()
    cnx_ut.close()
   
    assert test_case.equals(city_tier_mapped_df)

""
test_map_city_tier()


###############################################################################
# Write test cases for map_categorical_vars() function
# ##############################################################################    
def test_map_categorical_vars():
    """_summary_
    This function checks if map_cat_vars function is working properly by
    comparing its output with test cases provided in the db in a table named
    'categorical_variables_mapped_test_case'


    SAMPLE USAGE
        output=test_map_cat_vars()

    """    
    map_categorical_vars()
    
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    map_categorical_vars_df= pd.read_sql('select * from categorical_variables_mapped', cnx)
    
    cnx_ut= sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    test_case=pd.read_sql('select * from categorical_variables_mapped_test_case', cnx_ut)
    
    cnx.close()
    cnx_ut.close()
    
    assert test_case.equals(map_categorical_vars_df)

""
test_map_categorical_vars()


###############################################################################
# Write test cases for interactions_mapping() function
# ##############################################################################    
def test_interactions_mapping():
    """_summary_
    This function checks if test_column_mapping function is working properly by
    comparing its output with test cases provided in the db in a table named
    'interactions_mapped_test_case'


    SAMPLE USAGE
        output=test_column_mapping()

    """ 
    interactions_mapping()
    
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    interactions_mapping_df= pd.read_sql('select * from model_input', cnx)
    
    cnx_ut= sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    test_case=pd.read_sql('select * from interactions_mapped_test_case', cnx_ut)
    
    cnx.close()
    cnx_ut.close()
    print(interactions_mapping_df.head())
    
    assert test_case.equals(interactions_mapping_df)

""
test_interactions_mapping()

""

