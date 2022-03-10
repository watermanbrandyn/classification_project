import os
from env import host, username, password
from env import get_db_url 
import pandas as pd

def get_telco_data(use_cache = True):
    if os.path.exists('telco.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('telco.csv')
    print('Acquiring data from SQL db')
    query = '''
    SELECT * 
    FROM customers
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN contract_types USING (contract_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    df = pd.read_sql(query, get_db_url('telco_churn'))
    df.to_csv('telco.csv', index=False)
    return df