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


def pie_churn(train):
    '''
    Takes in the train df and outputs a pie chart showing the No Churn/Churn ratios 
    '''
    # Creates a list with the 'No Churn' and 'Churn' count totals by indexing the churn_Yes column
    churn_counts = [(train.churn_Yes.value_counts()[0]), (train.churn_Yes.value_counts()[1])]
    # Assigns labels for the pie chart
    labels = ['No Churn', 'Churn']
    # Establishes the inputs for the pie chart and displays the % with one decimal place
    plt.pie(churn_counts, labels=labels, autopct = '%.1f%%')
    plt.title('Churn Breakdown')
    plt.show()


def churn_corr(train):
    '''
    This function takes in our train df and displays a heatmap to show correlation to our target of churn. 
    '''
    # We don't want this column because it contains all unique values and is not going to be useful here.
    df = train.drop(columns='customer_id')
    # Establishing the parameters of our heatmap
    # Size of output 
    plt.figure(figsize=(10,10))
    # Title
    plt.title('Heatmap of Churn Correlation')
    # Configuring the actual heatmap
    sns.heatmap(df.corr()[['churn_Yes']].sort_values(by='churn_Yes',
        ascending=False), vmin=-1, vmax=1, annot=True, cmap='BuPu')


def phone_int(train, alpha):
    '''
    This function takes in our train df and established alpha value. It displays a bargraph 
    of the churn outcomes for customers with phone and internet plans. 
    We also run a chi^2 test on Phone and Internet plans and churn to test for independence. 
    Our hypothesis and conclusions from this are displayed.
    '''
    # For ease of use, we create a phone_int column from our encoded data, where phone service and internet are satisfied
    train['phone_int'] = ((train.phone_service_Yes == 1) & (train.internet_service_type_None == 0))
    # We need to make phone_int an int type
    train.phone_int = train.phone_int.astype(int)
    # We make a crosstab of phone_int with churn values
    phone_int_cross = pd.crosstab(train.phone_int, train.churn_Yes)
    # Creation of a stacked bargraph for visualization, with title and labels
    phone_int_cross.plot(kind='bar', stacked=True)
    plt.title('Churn for Phone and Internet Plans')
    plt.xlabel('Having Phone and Internet')
    plt.ylabel('Number of Customers')
    plt.show()
    
    # Establishing our hypothesis for statistical testing
    print('H0: Having a Phone and Internet plan and churn are independent of one another.')
    print('HA: Having a Phone and Internet plan and churn are not independent of one another.\n')
    # Using chi^2 because we are comparing two categorical variables
    chi2, p, degf, expected = stats.chi2_contingency(phone_int_cross)
    # Optional prints for display of observed and expected crosstabs
    # print('Observed\n')
    # print(phone_int_cross.values)
    # print('---\nExpected\n')
    # print(expected)
    # print('---\n')

    # Printing our chi^2 and p values
    print(f'chi^2 = {chi2: .4f}')
    print(f'p = {p:.4}\n')
    # Our alpha was already established (.05), comparing it to our given p value
    if p < alpha:
        print('Since our p-value is less than alpha we can reject the null hypothesis.')
    else: 
        print('Since our p-value is not less than alpha we cannot reject the null hypothesis.')


def fiber_churn(train):
    '''
    This function takes in our train dataframe and displays a stacked bargraph of the crosstab
    between Fiber and churn.
    '''
    # We make a crosstab of phone_int with churn values
    fiber_cross = pd.crosstab(train['internet_service_type_Fiber optic'], train.churn_Yes)
    # Creation of a stacked bargraph for visualization, with title and labels
    fiber_cross.plot(kind='bar', stacked=True)
    plt.title('Churn for Customers with Fiber')
    plt.xlabel('Having Fiber')
    plt.ylabel('Number of Customers')
    plt.show()

def senior_churn(train, alpha):
    '''
    This function takes in our train dataframe and established alpha value. It displays a bargraph
    of the crosstab between senior_citizen and churn. 
    It also displays our hypothesis and outcome for conducing a chi^2 analysis of senior_citizen 
    and churn. 
    '''
    # We make a crosstab of senior_citizen with churn values
    senior_cross = pd.crosstab(train.senior_citizen, train.churn_Yes)
    # Creation of a stacked bargraph for visualization, with title and labels
    senior_cross.plot(kind='bar', stacked=True)
    plt.title('Churn for Seniors')
    plt.xlabel('Being a Senior Citizen')
    plt.ylabel('Number of Customers')
    plt.show()
    
    # Establishing our hypothesis for statistical testing
    print('H0: Being a senior citizen and churn are independent of one another.')
    print('HA: Being a senior citizen and churn are not independent of one another.\n')
    # Using chi^2 because we are comparing two categorical variables
    chi2, p, degf, expected = stats.chi2_contingency(senior_cross)
    # Optional prints for display of observed and expected crosstabs
    # print('Observed\n')
    # print(phone_int_cross.values)
    # print('---\nExpected\n')
    # print(expected)
    # print('---\n')

    # Printing our chi^2 and p values
    print(f'chi^2 = {chi2: .4f}')
    print(f'p = {p:.4}\n')
    # Our alpha was already established (.05), comparing it to our given p value
    if p < alpha:
        print('Since our p-value is less than alpha we can reject the null hypothesis.')
    else: 
        print('Since our p-value is not less than alpha we cannot reject the null hypothesis.')


def monthly_cost(train, alpha):
    '''
    This function takes our train dataframe and established alpha. It displays a histplot of 
    our monthly_charges and churn. 
    It also displays our hypothesis and outcome of a 1-Tail Independent T-Test
    '''
    # Establishing our churn and not_churned groups for comparison
    churned = train[train.churn_Yes == 1]
    not_churned = train[train.churn_Yes == 0]
    # Our visualization of monthly_charges by churn
    # Histplot with title, labels, and a legend
    sns.histplot(data = churned.monthly_charges, label = 'Churned', color = 'red')
    sns.histplot(data = not_churned.monthly_charges, label = 'Not Churned', color = 'yellow')
    plt.title('Churn by monthly charges')
    plt.legend();
    plt.show()
    # Displaying our hypothesis
    print('H0: The average monthly charges for customers that churn <= the monthly charges for customers that do not churn.')
    print('HA: The average monthly charges for customers that churn > the monthly charges for customers that do not churn.\n')
    # Running our two-sample t-test
    t, p = stats.ttest_ind(churned.monthly_charges, not_churned.monthly_charges, equal_var=False)
    # Printing our t and p-value
    print(f't = {t: .4f}')
    print(f'p/2 = {(p/2):.4}\n')
    # Test against required conditions for t and p-value, t > 0 because we are doing a 1-tail with > for HA
    print()
    if t > 0 and (p/2) < alpha:
        print("We can reject our null hypothesis.")
    else:
        print("We fail to reject the null hypothesis.")

def tenure_churn(train, alpha):
    '''
    This function takes our train dataframe and established alpha. It displays a histplot of 
    our tenure and churn. 
    It also displays our hypothesis and outcome of a 1-Tail Independent T-Test
    '''
     # Establishing our churn and not_churned groups for comparison
    churned = train[train.churn_Yes == 1]
    not_churned = train[train.churn_Yes == 0]
    # Our visualization of monthly_charges by churn
    # Histplot with title, labels, and a legend
    sns.histplot(data = churned.tenure, label = 'Churned', color = 'red')
    sns.histplot(data = not_churned.tenure, label = 'Not Churned', color = 'yellow')
    plt.title('Churn by Tenure')
    plt.legend();
    plt.show()
      # Displaying our hypothesis
    print('H0: The average tenure for customers that churn >= the tenure for customers that do not churn.')
    print('HA: The average tenure for customers that churn < the tenure for customers that do not churn.\n')
    # Running our two-sample t-test
    t, p = stats.ttest_ind(churned.tenure, not_churned.tenure, equal_var=False)
    # Printing our t and p-value
    print(f't = {t: .4f}')
    print(f'p/2 = {(p/2):.4}\n')
    # Test against required conditions for t and p-value, t > 0 because we are doing a 1-tail with > for HA
    print()
    if t < 0 and (p/2) < alpha:
        print("We can reject our null hypothesis.")
    else:
        print("We fail to reject the null hypothesis.")


def payment_churn(train):
    '''
    This function takes our train dataframe and displays a stacked bargraph of all payment types
    against churn. It (re)creates a column for bank transfer auto payments from our encoded data.
    '''
    # Establish which columns we are plotting 
    columns = ['bank_transfer_auto', 'payment_type_Credit card (automatic)', 'payment_type_Electronic check', 'payment_type_Mailed check']
    # Creation of bank transfer column (as seen above) for ease of analysis from encoded data
    train['bank_transfer_auto'] = ((train['payment_type_Credit card (automatic)'] == 0) & (train['payment_type_Electronic check'] == 0) & (train['payment_type_Mailed check'] == 0))
    # Setting bank_transfer_auto to type int for consistency
    train.bank_transfer_auto = train.bank_transfer_auto.astype(int)
    # Loop to display bargraphs of payment type and churn
    for col in columns:
        cross = pd.crosstab(train[col], train.churn_Yes)
        cross.plot(kind='bar', stacked=True)
        plt.title(f'{col} and Churn')
        plt.xlabel('Has Payment Type')
        plt.ylabel('Customer Count')
        plt.show()


def contract_churn(train):
    '''
    This function takes our train dataframe and displays a stacked bargraph of all contract types
    against churn. It (re)creates a column for no contract from our encoded data.
    '''
    # Establish which columns we are plotting 
    columns = ['No_contract (Month to Month)', 'contract_type_One year', 'contract_type_Two year']
    # Creation of No contract column (as seen above) for ease of analysis from encoded data
    train['No_contract (Month to Month)'] = ((train['contract_type_One year'] == 0) & (train['contract_type_Two year'] == 0))
    # Setting No contract to type int for consistency
    train['No_contract (Month to Month)'] = train['No_contract (Month to Month)'].astype(int)
    # Loop to display bargraphs of payment type and churn
    for col in columns:
        cross = pd.crosstab(train[col], train.churn_Yes)
        cross.plot(kind='bar', stacked=True)
        plt.title(f'{col} and Churn')
        plt.xlabel('Has Contract Type')
        plt.ylabel('Customer Count')
        plt.show()