# Need pandas for dataframe maniuplations 
import pandas as pd
# Need numpy for calculation manipulations
import numpy as np
# Splitting function
from sklearn.model_selection import train_test_split

def prep_telco(df):
    '''
    Takes the Telco dataset and returns it after preparing/cleaning it.
        - drops unnecessary data/columns
        - modifies total_charges column to address empty value issue and change to proper type
            - drop the NaN values
        - encodes categorical columns and concats them to the telco_df
    Splits the data into train, validate, test using train_validate_test_split()
    Returns train, validate, test
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
    # Iterate through the categorical columns to encode them
    for col in cat_cols:
        dummy_df = pd.get_dummies(df[col],
                            prefix = df[col].name,
                            drop_first=True,
                            dummy_na=False)
        # Add the dummy vars to the df
        df = pd.concat([df, dummy_df], axis=1)
        # Delete the original (non-encoded) columns
        df = df.drop(columns=col)
    # Split our df in to train, validate, and test splits
    train, validate, test = telco_split(df)
    return train, validate, test
    
def telco_split(df):
    '''
    This function takes in a dataframe and returns train, validate, test splits.
    An initial 20% of data is split to place as 'test'
    A second split is performed (on the remaining 80%) between train and validate (70/30)
    '''
    # First split with 20% going to test
    train_validate, test = train_test_split(df, train_size = .8, 
                                                stratify= df.churn_Yes, random_state = 123)
    # Second split with 70% of remainder going to train, 30% to validate
    train, validate = train_test_split(train_validate, train_size = .7,
                                                stratify= train_validate.churn_Yes, random_state=123)
    # Return train, validate, test (56%, 24%, 20% splits of original df)
    return train, validate, test