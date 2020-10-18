import csv
import pandas as pd
import numpy as np


def generateNoise(sensitivity, paramLambda):
    return np.random.laplace(0,sensitivity/paramLambda, 1)


if __name__=="__main__":
    df = pd.read_csv('test.csv')
    for i in range(100):
        print(generateNoise(1,100))

