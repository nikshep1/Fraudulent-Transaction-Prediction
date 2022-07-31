# Fraudulent-Transaction-Prediction
A data science project to predict whether a transaction is a fraud or not.

<div align="center">
    <img alt="churn" src="https://www.finance-monthly.com/Finance-Monthly/wp-content/uploads/2018/07/Fraud-Epidemic-Costs-%C2%A33.2-Trillion-Globally.jpg" width="100%" height="300">
</div>

<br>

##  Business Problem

We need to deliver to the  Company a production model in which model classifies them as fraud or not fraud. The main aim is to predict whether the transactions happening in the account is fraudulent or not basis of the Balances at the opening and closing in the customer's account. The dataset shows us the Fraud not Fraud cases, but we need to analyze whether the selected fraud cases are real fraud cases or not. For detecting this we need to perform certain conditions to check and detect the dataset manually.

##  Solution Strategy

My solution to solve this problem will be the development of a data science project. This project will have a machine learning model which can predict whether a transaction is fraudulent or not.

*Step 01. Data Description:* In this first section the data will be collected and studied. The missing values will be threated or removed. Finally, a initial data description will carried out to know the data. Therefore some calculations of descriptive statistics will be made, such as kurtosis, skewness, media, fashion, median and standard desviation.

*Step 02. Feature Engineering:* In this section, a mind map will be created to assist the creation of the hypothesis and the creation of new features. These assumptions will help in exploratory data analysis and may improve the model scores.

*Step 03. Data Filtering:* Data filtering is used to remove columns or rows that are not part of the business. For example, columns with customer ID, hash code or rows with age that does not consist of human age.

*Step 04. Exploratory Data Analysis:* The exploratory data analysis section consists of univariate analysis, bivariate analysis and multivariate analysis to assist in understanding of the database. The hypothesis created in step 02 will be tested in the bivariate analysis.

*Step 05. Data Preparation:* In this fifth section, the data will be prepared for machine learning modeling. Therefore, they will be transformed to improve the learning of the machine learning model, thus they can be encoded, oversampled, subsampled or rescaled.

*Step 06. Feature Selection:* After the data preparation in this section algorithms, like Boruta, will select the best columns to be used for the training of the machine learning model. This reduces the dimensionality of the database and decreases the chances of overfiting.

*Step 07. Machine Learning Modeling:* Step 07 aims to train the machine learning algorithms and how they can predict the data. For validation the model is trained, validated and applied to cross validation to know the learning capacity of the model.

*Step 08. Hyparameter Fine Tuning:* Firstly selected the best model to be applied in the project, it's important to make a fine tuning of the parameters to improve its scores. The same model performance methods apllied in the step 07 are used.

*Step 09. Conclusions:* This is a conclusion stage which the generation capacity model is tested using unseen data. In addition, some business questions are answered to show the applicability of the model in the business context.

*Step 10. Model Deploy:* This is the final step of the data science project. So, in this step the flask api is created and the model and the functions are saved to be implemented in the api.

## Top 3 Data Insights

* #### All the fraud amount is greater than 10.000.

    *TRUE:* The values are greater than 10.000. But it's important to note that the no-fraud values is greater than 100.000 also.

    ![hypothesis2](![image](https://user-images.githubusercontent.com/108456495/181827922-499d2760-eb1f-4126-9448-116291925d93.png)

* #### 60% of fraud transaction occours using cash-out-type method.

    *FALSE:* The fraud transaction occours in transfer and cash-out type. However they're almost the same value.

    ![hypothesis3](![image](https://user-images.githubusercontent.com/108456495/181828070-94c613b5-42b9-4341-8a81-04d684cdc7cb.png))
    ![image](https://user-images.githubusercontent.com/108456495/181828156-4caf85b7-e516-42d2-a5b4-72563a52ba9b.png)


* #### Values greater than 100.000 occours using transfers-type method.

    *FALSE:* The majority transactions occours in trasnfer-type, however transactions greater than 100.000 occour in cash-out and cash-in too.

    ![hypothesis4](![image](https://user-images.githubusercontent.com/108456495/181828180-8a35457b-bba8-49ec-920b-5156b4d180ef.png))
    
    ## Distribution of transaction types
    ![image](https://user-images.githubusercontent.com/108456495/181828804-3d9ece42-bde0-4d07-9536-3878d9127387.png)
## AXES-SUBPLOT
![image](https://user-images.githubusercontent.com/108456495/181828927-3c03e53d-1659-471d-8cf4-e7a2eb99a498.png)
## Performed Models and their Accuracies(Before Under Sampling)
* ### Logistic Regression: 88.21% 

* ### XG Boost Classifier:  96.02%
## Under Sampling
### BEFORE  UNDERSAMPLING RATIO OF FRAUD AND NON-FRAUD DATA
![image](https://user-images.githubusercontent.com/108456495/181829326-e2a30260-de92-47d4-a766-7dbb1350c7d7.png)
### After  UNDERSAMPLING RATIO OF FRAUD AND NON-FRAUD DATA
![image](https://user-images.githubusercontent.com/108456495/181829425-8b12b459-4422-4395-8046-c94d2574ab8f.png)
## Performed Models and their Accuracies(After Under Sampling)
* ### Logistic Regression: 81.96% 

* ### XG Boost Classifier:  88.92%
# Final Model 
### XG Boost Classifier
#### With accuracy of 88.92%
