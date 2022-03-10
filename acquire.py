# os needed to do local inspection of cache, to see if data exists locally
import os
# env.py contains our credentials to access the SQL server we are pulling the data from
from env import host, username, password
# Pandas is needed to perform SQL interaction
import pandas as pd


def get_db_url(db_name, username=user, hostname=host, password=password):
    '''
    This function requires a database name (db_name) and uses the imported username,
    hostname, and password from an env file. 
    A url string is returned using the format required to connect to a SQL server.
    '''
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return url

def get_telco_data(use_cache = True):
    '''
    This function is used to acquire the Telco dataset from the SQL server. It has no 
    required inputs, and checks the cache to see if the requested data already exists locally.
    Creates a dataframe from the SQL query, and then uses that dataframe to create a csv file.
    Returns the dataframe that is created.
    '''
    # Checking to see if data already exists in local csv file
    if os.path.exists('telco.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('telco.csv')
    # If data is not local we will acquire it from SQL server
    print('Acquiring data from SQL db')
    # Query to refine what data we want to grab (all of it mostly)
    query = '''
    SELECT * 
    FROM customers
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN contract_types USING (contract_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    # Command line interaction with SQL server and assignment to dataframe (df)
    df = pd.read_sql(query, get_db_url('telco_churn'))
    # Creation of csv file
    df.to_csv('telco.csv', index=False)
    # Returns the dataframe
    return df