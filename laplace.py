import csv
import pandas as pd
import numpy as np
from normalize import *

def generateNoise(sensitivity, paramLambda):
    return np.random.laplace(0,sensitivity/paramLambda, 1)


if __name__=="__main__":
    df = pd.read_csv('test.csv')
    minVal=df["Age"].min()
    maxVal=df["Age"].max()
    print(minVal,maxVal)
    for i in range(100):
        print(48+generateNoise(28,1))
    print("\n")
    for i in range(100):
        print(denormalizeVal(1+generateNoise(1,1),minVal,maxVal))
