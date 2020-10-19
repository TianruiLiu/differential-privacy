'''
File Description:
This file contains a function to parse conditions from string to real conditions
and a function to return real results from a database

Author:
Tianrui Liu; Qingru Zhang
'''


# This is the function for return true result of a query from a given database.
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

# This is a function that parse a string of condition into a python condition
# The string is splitted in order to be parsed.
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
