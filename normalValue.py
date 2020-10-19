import csv
import pandas as pd
import numpy as np
from normalize import *

def trueResult(dataframe, conditionList, attribute, queryType):
    finalCondition = 1

    for condition in conditionList:
        finalCondition &= condition

    select=dataframe[finalCondition]

    result=0
    if queryType=="Count":
        result=select[attribute].count()
    elif queryType=="Sum":
        result=select[attribute].sum()
    elif queryType=="Min":
        result=select[attribute].min()
    elif queryType=="Max":
        result=select[attribute].max()
    elif queryType=="Mean":
        result=select[attribute].mean()
    return result


def parseCondition(dataframe, conditionString):

    conditionStringList=conditionString.split()
    attribute=conditionStringList[0]
    operator=conditionStringList[1]
    stringNumber=conditionStringList[2]
    number = eval(stringNumber)

    condition = 0
    if operator =="=":
        condition = dataframe[attribute] == number
    elif operator ==">":
        condition = dataframe[attribute] > number
    elif operator ==">=":
        condition = dataframe[attribute] >= number
    elif operator =="<":
        condition = dataframe[attribute] < number
    elif operator =="<=":
        condition = dataframe[attribute] <= number
    return condition

def parseNormalizedCondition(dataframe, conditionString,minVal,maxVal):

    conditionStringList=conditionString.split()
    attribute=conditionStringList[0]
    operator=conditionStringList[1]
    stringNumber=conditionStringList[2]
    number = eval(stringNumber)
    number = (number-minVal)/(maxVal-minVal)

    condition = 0
    if operator =="=":
        condition = dataframe[attribute] == number
    elif operator ==">":
        condition = dataframe[attribute] > number
    elif operator ==">=":
        condition = dataframe[attribute] >= number
    elif operator =="<":
        condition = dataframe[attribute] < number
    elif operator =="<=":
        condition = dataframe[attribute] <= number
    return condition


if __name__=="__main__":

    df = pd.read_csv('test.csv')

    conditionList=[df["Age"] > 30, df["Age"] < 40]


    result=trueResult(df,conditionList,"Age","Count")
    print(result)
