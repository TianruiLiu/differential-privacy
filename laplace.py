import numpy as np

# This is the core of Laplace mechanism. It generate noise based on the sensitivity and lambda of a query.
def generateNoise(sensitivity, paramLambda):
    return np.random.laplace(0,sensitivity/paramLambda, 1)

