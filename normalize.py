import csv
import pandas as pd
import numpy as np

def normalize(dataframe,attribute,minVal,maxVal):
    dataframe[attribute]=(dataframe[attribute]-minVal)/(maxVal-minVal)

def normalizeDatabase(dataframe):
    normalizedDataframe=dataframe.copy(deep=True)
    for column in normalizedDataframe.select_dtypes(exclude='object'):
        minVal=normalizedDataframe[column].min()
        maxVal=normalizedDataframe[column].max()
        normalize(normalizedDataframe,column,minVal,maxVal)
    return normalizedDataframe

def normalizeVal(val,minVal,maxVal):
    val = (val-minVal)/(maxVal-minVal)
    return val

def denormalizeVal(val,minVal,maxVal):
    val = val * (maxVal-minVal) +minVal
    return val

if __name__=="__main__":
    df = pd.read_csv('test.csv')
    normalizeDatabase(df)
    print(df)

