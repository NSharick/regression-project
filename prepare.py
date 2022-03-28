## Data Preparation Functions for the regression module project ##

#imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import f_regression, SelectKBest, RFE

#prep data function
def prep_data(df):
    df = df.dropna()
    return df

#Split data function
def split_data(df):
    '''
    this function takes the full dataset and splits it into three parts (train, validate, test) 
    and returns the resulting dataframes
    '''
    train_val, test = train_test_split(df, train_size = 0.8, random_state=123)
    train, validate = train_test_split(train_val, train_size = 0.7, random_state=123)
    return train, validate, test

#remove outliers function
def remove_outliers(df, k, col_list):
    ''' this function will remove outliers from a list of columns in a dataframe 
        and return that dataframe. A list of columns with significant outliers is 
        assigned to a variable in the below wrangle function and can be modified if needed
    '''
    #loop throught the columns in the list
    for col in col_list:
        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        iqr = q3 - q1   # calculate interquartile range
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound
        # return dataframe without outliers
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)] 
    return df

#split dataset by region function
def split_by_region(df):
    df1 = df[df['fips']==6037.0]
    df2 = df[df['fips']==6059.0]
    df3 = df[df['fips']==6111.0]
    return df1, df2, df3

