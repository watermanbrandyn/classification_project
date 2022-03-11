# Reducing Telco Churn (Classification Project)

## Project Goals 
The goal of this analysis is to provide insights and recommendations that reduce overall churn of Telco customers. This will be done by identifying
some of the key drivers of churn, applying these to classification models in order to best predict churn, and then providing some recommendations that 
can best serve Telco to avoid future churn.

## Project Description
Constant insight into why customers churn is incredibly important for any business. It is well established that customer acquisition is more expensive than retention,
and above all a grasp on a customer's lifetime value (CLV) can enable a business to make the correct choices in relation to self and customer. With the necessity of internet and phone services in modern work and play these realities apply even moreso to Telco and the ability to predict, and prevent, churn would undoubtedly increase profit margins and guarantee business longevity. Through the analysis of the telco_churn data, gathered from Codeup's SQL server, we can identify churn factors, curate models to help predict churn, and apply recommendations to reduce overall churn moving forward.

## How to Reproduce this Work
If someone wishes to reproduce the work done in this project you can:
- Clone my repo; ensure you grab the acquire.py and prepare.py modules, and properly set up a .gitignore
- Have your own env.py file that contains your credentials to access the SQL server, this should be stored locally
- Use of the pandas, numpy, matplotlib, seaborn, and sklearn libraries
- Follow along/run the Final Report

## Initial Questions
With a brief glance at the data some of the following were my initial questions:
- How does the type of service impact churn? (Phone, Internet, Internet & Phone)
- How does the specific internet type impact churn? (DSL/Fiber)
- Is there an attribute of demographic that impacts churn? (Senior citizen, 
