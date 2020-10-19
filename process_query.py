from laplace import *
from normal_query import *
import pandas as pd

def processOneQuery(dataframe, conditionStringList, attribute, queryType,paramLambda):
    conditionList=[]

    paramLambda = int(paramLambda)
    minVal = dataframe[attribute].min()
    maxVal = dataframe[attribute].max()
    sensitivity = 0

    if (queryType =="Count"):
        sensitivity = 1
    elif (queryType=="Max" or queryType=="Min" or queryType=="Sum"):
        sensitivity = maxVal - minVal

    for ele in conditionStringList:
        conditionList.append(parseCondition(dataframe,ele))

    clearResult = trueResult(dataframe,conditionList,attribute,queryType)

    if (queryType=="Count" or queryType=="Max" or queryType=="Min" or queryType=="Sum"):
        return clearResult+generateNoise(sensitivity,paramLambda)

    if (queryType=="Mean"):
        clearSumResult = trueResult(dataframe, conditionList, attribute, "Sum")
        clearCountResult = trueResult(dataframe,conditionList,attribute,"Count")
        sensitivity = (maxVal-minVal)/clearCountResult
        noiseResult = clearSumResult/clearCountResult + generateNoise(sensitivity,paramLambda)
        return noiseResult

if __name__=="__main__":
    df = pd.read_csv('test.csv')
    conditionStringList=["Age > 20", "Age < 30"]
    for i in range(100):
        result=processOneQuery(df,conditionStringList,"Age", "Count", 1)
        print(result)

