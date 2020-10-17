from laplace import *
from normalize import *
from normalValue import *

def processOneQuery(dataframe, conditionStringList, attribute, queryType,sensitivity,paramLambda):
    conditionList=[]
    conditionNormalizedList=[]
    minVal = dataframe[attribute].min()
    maxVal = dataframe[attribute].max()


    normalizedDataframe=normalizeDatabase(dataframe)
    for ele in conditionStringList:
        conditionList.append(parseCondition(dataframe,ele))

    for ele in conditionStringList:
        conditionNormalizedList.append(parseNormalizedCondition(normalizedDataframe,ele,minVal,maxVal))

    normalizedCleanResult = trueResult(normalizedDataframe,conditionNormalizedList,attribute,queryType)
    normalizedNoiseResult = normalizedCleanResult + generateNoise(sensitivity,paramLambda)

    if (queryType=="Count"):
        return normalizedNoiseResult
    if (queryType=="Max" or queryType=="Min"):
        noiseResult=denormalizeVal(normalizedNoiseResult,minVal,maxVal)
        return noiseResult
    if (queryType=="Sum"):
        clearResult=trueResult(dataframe,conditionList,attribute,queryType)
        noiseResult=clearResult+denormalizeVal(generateNoise(1,1),minVal,maxVal)
        return noiseResult
    if (queryType=="Mean"):
        clearSumResult = trueResult(dataframe, conditionList, attribute, "Sum")
        clearCountResult = trueResult(dataframe,conditionList,attribute,"Count")
        noise=generateNoise(1,1)
        denormalizedNoise=denormalizeVal(noise,minVal,maxVal)
        noiseSum = clearSumResult+denormalizedNoise
        noiseResult = noiseSum/clearCountResult
        return noiseResult

if __name__=="__main__":
    df = pd.read_csv('test.csv')
    conditionStringList=["Age > 30", "Age < 40"]
    result=processOneQuery(df,conditionStringList,"Age", "Max", 1, 1)
    print(result)

