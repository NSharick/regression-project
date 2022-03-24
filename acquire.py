## Acquire function for the zillow dataset - regression project ##

#Imports for the function:
import numpy as np
import pandas as pd
from env import get_db_url
import os


def acquire_zillow():
    '''
    This function checks for a copy of the dataset in the local directory 
    and pulls a new copy and saves it if there is not one,
    it then cleans the data by removing significant outliers then
    removing the rows with null values for 'yearbuilt'
    '''
    #assign the file name
    filename = 'zillow.csv'
    #check if the file exists in the current directory and read it if it is
    if os.path.exists(filename):
        print('Reading from csv file...')
        #read the local .csv into the notebook
        df = pd.read_csv(filename)
        return df
    #assign the sql query to a variable for use in pulling a new copy of the dataset from the database
    query = '''
    SELECT pro.bedroomcnt, pro.bathroomcnt, pro.calculatedfinishedsquarefeet, pro.taxvaluedollarcnt, pro.yearbuilt, pro.fips
    FROM properties_2017 AS pro
    JOIN predictions_2017 AS pre USING(parcelid)
    WHERE pro.propertylandusetypeid = 261
    '''
    #if needed pull a fresh copy of the dataset from the database
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, get_db_url('zillow'))
    #save a copy of the dataset to the local directory as a .csv file
    df.to_csv(filename, index=False)
    return df