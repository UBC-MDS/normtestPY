'''
This script tests the function from params_mle.py

The function fits data to a Guassian distribution using Maximum Likelihood Estimation (MLE)
Input:  DATAFRAME where data for each continous variable is in its
        respective column
Output: DATAFRAME where the first row contains the estimated means and
        the second row contains the estimated variance, and the columns
        present the original variables in the data
'''

import pytest
from normtestPY.params_mle import params_mls

# Unit Tests
