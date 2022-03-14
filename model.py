# manipulations
import pandas as pd
import numpy as np

# viz
import seaborn as sns
import matplotlib.pyplot as plt

# math
from scipy import stats
import statistics
import math

# sklearn suite
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.tree import export_graphviz, export_text
from sklearn.metrics import classification_report, confusion_matrix, recall_score, precision_score
from sklearn.metrics import f1_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

def more_clean(train, validate, test):
    '''
    This function takes in our test, validate, and test dataframes and returns the selected feature versions as test10
    validate10, and test10. It also separates the customer_id columns and retains it for posterity, returning train_cust
    validate_cust, and test_cust as dataframes for the purpose of indexing. 
    '''
    # Establish what features are moving forward to modeling 
    features = ['senior_citizen', 'tenure', 'monthly_charges', 'churn_Yes', 'internet_service_type_Fiber optic',
                'contract_type_One year', 'contract_type_Two year', 'payment_type_Credit card (automatic)',
                'payment_type_Electronic check', 'payment_type_Mailed check']
    # Retain customer_id for posterity 
    train_cust = train[['customer_id']]
    validate_cust = validate[['customer_id']]
    test_cust = test[['customer_id']]
    # Retain only columns that are not included in features
    train10 = train[train.columns[train.columns.isin(features)]]
    validate10 = validate[validate.columns[validate.columns.isin(features)]]
    test10 = test[test.columns[test.columns.isin(features)]]

    return train10, validate10, test10, train_cust, validate_cust, test_cust