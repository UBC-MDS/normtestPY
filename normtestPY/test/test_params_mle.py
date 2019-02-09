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
import pandas as pd
import numpy as np
from normtestPY.params_mle import params_mle

# Dummy data for testing
dummy = pd.DataFrame({"var1": [0,1,1,-1], "var2": [-1, -1, 0, 1]})
expected = pd.DataFrame({"var1": [1/4, (11/16)**(1/3)], "var2": [2,3]})

# Unit tests

# Test for the most common case where input is a df
# Check for correct output type, and calculations
def test_params_mle():
    results = params_mle(dummy)

    assert isinstance(params_mle(dummy), pd.DataFrame)
    assert np.allclose(results, expected)

# Test for other possible input types
def test_non_df_inputs():
    series_type = (dummy["var1"])
    matrix_type = np.array(dummy)
    list_2d_type = list([list(dummy["var1"]), list(dummy["var2"])])

    assert np.allclose(params_mle(series_type), expected["var1"])
    assert np.allclose(params_mle(matrix_type), expected)
    assert np.allclose(params_mle(list_2d_type), expected)
    assert isinstance(params_mle(matrix_type), pd.DataFrame)
    assert isinstance(params_mle(list_2d_type), pd.DataFrame)
    assert isinstance(params_mle(series_type, pd.DataFrame))

# Test for empty inputs
def test_empty inputs():
    
# Exception handling
