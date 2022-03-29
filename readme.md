# Regression Project - Zillow Dataset

### Project Description:
- The data science team at zillow are looking to improve their model for predicting home prices of single family residences. This project will explore the zillow dataset looking at the interactions of different variables and how they can inprove the model's predictive value. Then it will develop different regression models for predicting home prices and evaluate their performance to provide more insight to the team. Lastly, based on the exploration and modeling, the project will provide actionable recomendations for the data science team to further develop the project. 

### Project Goals:
- Goal 1: My first goal is to explore the zillow dataset and find which features have the strongest relationship with home prices and will provide the most value to the model's predictive ability

- Goal 2: My second goal is to develop multiple predictive models based on a wide range of input features and model hyperparameters and evaluate their performance and end with the best performing model to move forward with.

- Goal 3: My third goal is to provide the team with insight on what region / county that the properties in the data set are located and how that impacts the drivers of home values.

- Goal 4: My fourth goal is to provide actionable recomendations for further development of the project.

### Initial Questions:
- Question 1: Is the square footage of the home related to its sale price?

- Question 2: Is the year the home was built related to its sale price?

- Question 3: Is the number of bedrooms a home has related to its sale price ?

- Question 4: Is the number of bathrooms a home has related to its sale price?

### Data Dictionary:

| Variable | Meaning |
|----------|---------|
|taxvaluedollarcnt|Home sale price for homes sold in 2017|
|yearbuilt|Year that the home was built|
|calculatedfinishedsquarefeet|Square footage of the home|
|bedroomcnt|Number of bedrooms in the home|
|bathroomcnt|Number of bathrooms in the home|
|fips|Federal information processing standards - for this project specifically relating to location of the property with the first two numbers representing the state and the last three numbers representing the county code. In this data set the values in the fips column are missing a leading '0' for the state code of '06' representing the state of California|

### Project Planning:

- First, write a function to pull the correct dataset from the database and save it as a csv in the local directory.

- Save the data acquision function in a seperate acquire.py file for future use

- Then, write a function that prepares the data by dealing with missing values, removing unneeded columns, and encoding categorical variables and scaling data as needed for use in machine learning models

- The data preparation function should also split the dataset into train, validate, and test sets for modeling

- Save the data preparation function in a acquire.py file for later use

- Document four specific questions that will be asked of the data to guide the data exploration

- Explore the data by visualizing key features related to the questions and how they relate to customer churn

- Continue to explore the data by running statistical tests to verify statistical significance of the relationships between the variables

- Document initial takeaways from the data exploration

- Develop initial regression machine learning models using the features identified in the exploration phase

- Refine those models using the train dataset by adjusting feature input and hyperparameter values

- Document the models performance on the train dataset

- Choose the three best performing models to validate using the validate dataset

- Document the performance of the models on the validate dataset

- Choose the model that performed the best and best fit the needs of the buisness question and test it using the test dataset

- Document key findings, recomendations, and next steps

### How to Reproduce this Project and Findings:

To reproduce my findings on this project you will need:

- An env file with you own credentials (hostname, username, password) to access the database and pull the zillow dataset

- The acquire.py file in this repository to pull the correct data from the database

- The prepare.py file in this repository to clean and split the dataset

- The jupyter notebook in this repository named "final_report_regression_project" which contains the code used to produce the project including the random_state identifiers to make sure and randomization of the data is consistent.

- Libraries used are numpy, pandas, seaborn, sklearn, scipy, and matplotlib. All imports are included at the top of the notebook.

### Key Findings:

- Goal 1 was to explore the zillow dataset and find features with the strongest relationship to home prices and that could be used to improve the predictive model. The best features found during data exploration were the home's square footage, the year the home was built, the number of bedrooms the home has and the number of bathrooms the home has.

- Goal 2 was to find the best performing predictive regression model that can be used to gain further insight on predicting home price. This project found that the polynomial model with only interactions and with square footage, year built, bathroom count, and bedroom count as input features performed the best. Further investigation on improving the model's performance resulted in a 69.5% improvement in reduction of root mean squared error by splitting the dataset into three datasets based on region (fips code).

- Goal 3 was to provide insight into what region the homes were located in. The dataset has a column labeled 'fips' which is the Federal information processing standards - for this project specifically relating to location of the property with the first two numbers representing the state and the last three numbers representing the county code. In this data set the values in the fips column are missing a leading '0' for the state code of '06' representing the state of California.
    - fips code 06037 = Los Angeles, CA
    - fips code 06059 = Orange County, CA
    - fips code 06111 = Ventura County, CA
    
- Goal 4 was to provide actionable recomendations which are included in the section below

### Recomendations:

- Since so many of the features in the zillow dataset had a significant amount of missing values it would be valueable to find other sources of historical data for the homes in the dataset and see if some of those values could be filled. In many cases over half of the observations had missing values in a column and using a measure of central tendencey to fill the values did not provide valuable information.

- The best performing model from this project should be compared to the current model to evaluate performance differences and to inform updates to the current model.

- Since splitting the data by region and modeling each region seperately increased the model's performance the current model should also be tested with the data split by region to see how it impacts the model's performance.

### Next Steps:

- Further investigation into features that relate to home price is needed to develop a more accurate model. This will be especially important if updated data that fills in the missing values is obtained.

- This project found that splitting the dataset by region then modeling each seperately increased the model's accuracy but it was only the first step in exploring this feature manipulation and it should be explored further.

