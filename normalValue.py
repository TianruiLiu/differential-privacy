import csv
import pandas as pd
import numpy as np


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


if __name__=="__main__":

    df = pd.read_csv('test.csv')
    conditionList=[]
    condition1 = "Age > 30"
    condition2 = "Age < 40"

    conditionList.append(parseCondition(df,condition1))
    conditionList.append(parseCondition(df,condition2))

    result=trueResult(df,conditionList,"Height(cm)","Max")

    print(result)