import pandas as pd
from scipy.stats import bernoulli

def limeNLP(blackbox, x0:str, nFeatures:int=3, nIter:int=100, p:float=0.2, random_state=42):
    """
    limeNLP receives a blackbox model, evaluates it at `x0` and returns a parsimonious explanation
    containing its `nFeatures` most influential words.

    blackbox:
        The model to be explained using LIME.
        `blackbox` must be able to evaluate the expression `blackbox(x0)` and return a prediction.

    x0 (str):
        The point of interest at which `blackbox` is to be explained.
        `x0` will be passed to `blackbox` as `blackbox(x0)` and must therefore be a string.
    
    nFeatures:
        Number of words that the explanation should contain.
        `limeNLP` will return a table with `nFeatures` words and their corresponding weight.
    
    nIterations:
        Defines how many `x0` will be perturbed.
        To create a perturbed instance, each word in `x0` will be either kept or dropped according
        to a Bernoulli distribution.
        At most, `nIter` instances will be generated because duplicates are removed.
    
    p (float):
        The probability parameter of a Bernoulli random variable with which each word in `x0` will
        be kept or dropped.
    
    random_state (int):
        Seed used to generate the data set of perturbed instances.
    """

    # Initialize bernoulli random variable
    B = bernoulli(p=1-p)

    # Initialize empty list to store perturbed instances in
    D = []

    # 