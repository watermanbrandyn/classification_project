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


def feature_selection(train, validate, test):
    '''
    This function takes in our test, validate, and test dataframes and returns the selected feature versions as test8
    validate8, and test8. It also separates the customer_id columns and retains it for posterity, returning train_cust
    validate_cust, and test_cust as dataframes for the purpose of indexing. 
    '''
    # Establish what features are moving forward to modeling 
    features = ['senior_citizen', 'tenure', 'monthly_charges', 'churn_Yes', 'internet_service_type_Fiber optic',
                'contract_type_One year', 'contract_type_Two year', 'payment_type_Electronic check']
    # Retain customer_id for posterity 
    train_cust = train[['customer_id']]
    validate_cust = validate[['customer_id']]
    test_cust = test[['customer_id']]
    # Retain only columns that are not included in features
    train8 = train[train.columns[train.columns.isin(features)]]
    validate8 = validate[validate.columns[validate.columns.isin(features)]]
    test8 = test[test.columns[test.columns.isin(features)]]

    return train8, validate8, test8, train_cust, validate_cust, test_cust

def get_baseline(train8):
    '''
    This function takes in our feature train dataframe and prints the baseline value. This baseline is based on the mean of
    the most common occurrence for our data.
    '''
    baseline = (train8.churn_Yes == 0).mean()
    baseline_rounded = round((baseline * 100), 2)
    print(f'Baseline: {baseline_rounded}%')


def x_y_separate(train8, validate8, test8):
    '''
    This function takes our feature dataframes (train, validate, test) and returns our x and y componenets. Where x is our features to model
    and y is our target variable (churn_Yes).
    '''
    x_train = train8.drop(columns='churn_Yes')
    y_train = train8.churn_Yes
    x_validate = validate8.drop(columns='churn_Yes')
    y_validate = validate8.churn_Yes
    x_test = test8.drop(columns='churn_Yes')
    y_test = test8.churn_Yes
    return x_train, y_train, x_validate, y_validate, x_test, y_test


def knn_model(x_c, y_c):
    '''
    This function takes in our x and y components of our dataframes and prints out the evaluation metrics
    for our KNN model. It creates the KNN model, fits it, and then analyzes the metrics.
    '''
    # Creation of our model with standard arguments
    knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
    # Fitting our data to our model
    knn.fit(x_c, y_c)
    # Creating our y_pred for the model
    y_pred = knn.predict(x_c)
    # Creating our y_pred_proba for the model
    y_pred_proba = knn.predict_proba(x_c)
    # Evaluation metrics are printed
    accuracy = knn.score(x_c, y_c)
    conf = confusion_matrix(y_c, y_pred)
    class_report = pd.DataFrame(classification_report(y_c, y_pred, output_dict=True)).T
    conf = confusion_matrix(y_c, y_pred)
    tpr = conf[1][1] / conf[1].sum()
    fpr = conf[0][1] / conf[0].sum()
    tnr = conf[0][0] / conf[0].sum()
    fnr = conf[1][0] / conf[1].sum()
    print(f'''
    The accuracy for our model is {accuracy: .4})
    The True Positive Rate is {tpr:.3}, The False Positive Rate is {fpr:.3},
    The True Negative Rate is {tnr:.3}, and the False Negative Rate is {fnr:.3}
    ''')
    print(class_report)


def random_forest(min_samples, max_depth, x_c, y_c):
    '''
    This function takes in our manipulated hyperparameters of min_samples_leaf and max_depth as well as our x and y components of our train, validate,
    or test dataframes. It outputs our evaluation metrics after creating, fitting, and utilizing a random forest classification model. 
    '''
    # Creation of our model parameters. All of these other than min_samples_leaf, max_depth, and random_state are defaults.
    # min_samples_leaf and max_depth will be manipulated to change our model outcomes and random_state will remain the same for reproducibility.
    rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini', min_samples_leaf=min_samples,
                           n_estimators=100, max_depth=max_depth, random_state=123)
    # Fitting our model
    rf.fit(x_c, y_c)
    # Our predictions are made
    y_pred = rf.predict(x_c)
    # Prediction probabilities
    y_pred_proba = rf.predict_proba(x_c)
    # Evaluation metrics are printed
    accuracy = rf.score(x_c, y_c)
    conf = confusion_matrix(y_c, y_pred)
    class_report = pd.DataFrame(classification_report(y_c, y_pred, output_dict=True)).T
    conf = confusion_matrix(y_c, y_pred)
    tpr = conf[1][1] / conf[1].sum()
    fpr = conf[0][1] / conf[0].sum()
    tnr = conf[0][0] / conf[0].sum()
    fnr = conf[1][0] / conf[1].sum()
    print(f'''
    The accuracy for our model is {accuracy: .4})
    The True Positive Rate is {tpr:.3}, The False Positive Rate is {fpr:.3},
    The True Negative Rate is {tnr:.3}, and the False Negative Rate is {fnr:.3}
    ''')
    print(class_report)


def random_forest_csv(min_samples, max_depth, x_c, y_c, cust_id):
    '''
    This function will take in our hyperparameters for our Random Forest model (the best performing one preferably), the x and y components of our test dataframe
    and the cust_id's for our test dataframe and create a .csv prediction file that contains customer_id, churn_probability, and churn_prediction.
    '''
    # Creation of our model parameters. All of these other than min_samples_leaf, max_depth, and random_state are defaults.
    # min_samples_leaf and max_depth will be manipulated to change our model outcomes and random_state will remain the same for reproducibility.
    rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini', min_samples_leaf=min_samples,
                           n_estimators=100, max_depth=max_depth, random_state=123)
    # Fitting our model
    rf.fit(x_c, y_c)
    # Our predictions are made
    y_pred = rf.predict(x_c)
    # Prediction probabilities, with the churn selected
    y_pred_proba = rf.predict_proba(x_c)[:,1]
    # Create our predictions dataframe
    predictions = pd.DataFrame(columns=['customer_id', 'churn_probability', 'churn_prediction'])
    # Add our customer_ids
    predictions['customer_id'] = cust_id.customer_id
    # Add our prediction probabilities
    predictions['churn_probability'] = y_pred_proba
    # Add our predictions
    predictions['churn_prediction'] = y_pred
    # Set customer_id as the index
    predictions = predictions.set_index('customer_id')
    # Write to a .csv file
    predictions.to_csv('test_predictions.csv')




