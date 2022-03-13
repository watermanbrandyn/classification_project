![Logo of the project](https://raw.githubusercontent.com/jehna/readme-best-practices/master/sample-logo.png)

# Reducing Telco Churn (Classification Project)

## Table of Contents
- [Project Goal](#project-goal)
- [Project Description](#project-description)
- [How to Reproduce](#how-to-reproduce)
- [Initial Questions](#initial-questions)
- [Data Dictionary](#data-dictionary)
- [Project Plan](#project-plan)
   - [Wrangling](#wrangling)
      - [Acquire](#acquire)
      - [Preparation and Splitting](#preparation-and-splitting)
  - [Exploration](#exploration)
  - [Modeling](#modeling)
  - [Deliverables](#deliverables)
    - [Final Report](#final-report)
    - [Modules](#modules)
    - [Predictions](#predictions)
- [Summary and Recommendations](#summary-and-recommendations)

## Project Goal
> The goal of this project is to offer analysis that can help reduce the churn of customers at Telco. 
This will be done by identifying some of the key drivers of churn, creating models to help predict vulnerable customers, and offering recommendations to avoid these possible churns.   

## Project Description
It is well established that the cost of acquiring a new customer far exceeds the cost of retaining a current one. With the need for phone and internet services in modern-day work and play this business reality becomes even more important to recognize for companies like Telco. A proper analysis of churn factors, and the subsequent solutions that arise, can greatly assist in keeping the company profitable as well as ensuring longevity and relevancy for years to come. Through identification of key factors in churn we can assist in predicting these vulnerabilities, address them with solutions, and help Telco retain market share of an essential industry while improving Customer Lifetime Values (CLV) and real-time margins. 

## How to Reproduce
To reproduce the outcomes in this project:
1. Have an env.py file with credentials (hostname, username, password) to access a SQL database that contains Telco data. Codeup's 'telco_churn' data was utilized
   for this project. 
2. Clone this repo and ensure you have all of the necessary modules and notebooks. Confirm that the .gitignore includes your env.py file to secure credentials.
3. Use of these libraries: pandas, numpy, matplotlib, seaborn, sklearn.
4. Be able to run the 'Final Report' jupyter notebook file. 
   - Supplemental 'classification_workbook' may also be useful in identifying some of the steps taken prior to the cleaner final code 

## Initial Questions


## Data Dictionary

## Project Plan
This project will start with some initial planning and question exploration before we even access the data. The question exploration has been delved out in the _Initial Questions_ section. 
Additionally let us detail what is to be provided at the conclusion of this project:
 - This README.md
 - Final Report.ipynb 
 - Workbooks and modules used

Moving forward we will **wrangle (acquire/prepare)** our data, **explore** for insights on key drivers, create **models** for prediction, and apply the best ones for the purpose of curating some **predictions**. This will all be **summarized** and **recommendations** for Telco will be provided. 

### Wrangling
This section contains our acquisition and preparation of the data.
#### Acquire
The acquire.py file contains the code that was used for acquiring the 'telco_churn' data. There is a **get_db_url()** function that is used to format the credentials for interacting with a SQL server, and the **get_telco_data()** function that queries the SQL server for the data. For this project Codeup's 'telco_churn' SQL database was used. The env.py file used, and the credentials within, are not included in this project and as covered under _How To Reproduce_ must be curated with one's own information.

#### Preparation and Splitting
The prepare.py file contains the code that was used for preparing the data. There is a **telco_split()** function that is used to create a train, validate, and test splits (3 dataframes) of the prepared dataframe. These splits are 56% train, 24% validate, and 20% test from the prepared dataframe. The **prep_telco()** function takes the acquired dataframe and cleans it for our exploratory purposes. Within this function the **telco_split()** function is utilized. 

### Exploration
For exploration only our train dataframe is used and...


### Modeling

### Deliverables

#### Final Report

#### Modules

#### Predictions

## Summary and Recommendations



## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

```shell
packagemanager install awesome-project
awesome-project start
awesome-project "Do something!"  # prints "Nah."
```

Here you should say what actually happens when you execute the code above.
