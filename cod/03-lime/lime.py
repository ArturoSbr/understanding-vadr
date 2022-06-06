import pandas as pd
from scipy.stats import bernoulli
from sklearn.linear_model import Lasso

# `nlp` class
class nlp:
    """
    Initialize an NLP explanation using LIME.

    `x0` (str):
        The point of interest at which the blackbox model is to be explained.
    
    `blackbox`:
        The model to be explained using LIME.
        `blackbox` must be able to evaluate the expression `blackbox(x0)` and return a prediction.
    """
    def __init__(self, blackbox, x0:str):
        nlp.x0 = x0
        nlp.words = x0.split(' ')
        nlp.blackbox = staticmethod(blackbox)

    # Method to create multiple perturbations stemming from x0
    def perturb(self, nIter:int=100, p:float=0.2, random_state:int=None):
        """
        `perturb` returns the perturbed instances that stem from `x0`. Each modified instance is weighted
        according to its similarity to `x0` and is scored by the blackbox model.
        
        Returns: A `pandas.DataFrame` object.
        
        `nIter` (int):
            Defines how many perturbation will be created from `x0`.
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

        # Create perturbed instances
        for i in range(nIter):
            if random_state is None:
                D.append(list(B.rvs(size=len(self.words))))
            if random_state is not None:
                D.append(list(B.rvs(size=len(self.words), random_state=random_state+i)))
        
        # Perturbed data to pandas.DataFrame object
        D = pd.DataFrame(data=D, columns=self.words)

        # Drop duplicates
        D = D.drop_duplicates().reset_index(drop=True)

        # Assign weights based on similarity to x0
        D['weight'] = D.sum(axis=1) / len(self.x0)

        # Initialize empty list to store scores in
        scores = []

        for i in D.index.values:
            # Extract modified version of text
            mod = D.iloc[i]
            mod = ' '.join(list(mod[mod > 0].index.values))

            # Append score to list
            scores.append(self.blackbox(mod))
        
        # Assign new scores
        D['pred'] = scores

        # Return Data.Frame
        self.data = D

    # Fit parsimonious modles until explanation is achieved
    def fit(self, nFeatures=3):
        """
        `fit()` fits a Lasso model (L1 penalty)
        """
        # Super low penalty
        penalty = 0.01

        # Initialize first Lasso
        m = Lasso(alpha=penalty, fit_intercept=False)

        # First fit
        m.fit(
            X=self.data[self.words],
            y=self.data['pred'],
            sample_weight=self.data['weight']
        )

        # Keep fitting until nFeatures is achieved
        while (sum(m.coef_ > 0) > nFeatures) and (penalty < 1):
            # Marginally increase penalty
            penalty += 0.01

            # Initialize Lasso with new penalty
            m = Lasso(alpha=penalty, fit_intercept=False)

            # Fit new Lasso
            m.fit(
                X=self.data[self.words],
                y=self.data['pred'],
                sample_weight=self.data['weight']
            )
        
        # Explanation
        E = pd.DataFrame({'word':self.words, 'importance':m.coef_})

        # Only non-zero coefficients
        E = E[E['importance'] > 0]

        # Sort by importance
        E = E.sort_values('importance', ascending=False).reset_index(drop=True)

        # Return explanation
        self.explanation = E
