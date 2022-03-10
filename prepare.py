# Need pandas for dataframe maniuplations 
import pandas as pd
import numpy as np

def prep_telco(df):
    '''
    Takes the Telco dataset and returns it after preparing/cleaning it.
        - drops unnecessary data/columns
        - modifies total_charges column to address string issue and change to proper type
        - encodes categorical columns and concats them to the telco_df


    '''
    # Drop any duplicates
    df.drop_duplicates(inplace=True)
    # Drop duplicated columns
    df = df.drop(columns=['customer_id', 'internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    # Replaces empty string total_charges as NaN values and converts the column to float
    df.total_charges = df.total_charges.replace(' ', np.nan).astype(float)
    # Drop the NaN values
    df.dropna(inplace=True)
    # Create a list of categorical columns
    cat_cols = [col for col in df.columns if df[col].dtype == 'O']




    return df
    
