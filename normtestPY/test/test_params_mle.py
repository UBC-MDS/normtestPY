'''
This script tests the function from params_mle.py

Parameters
----------
None

Returns
-------
Assertion errors if tests fail
'''

# Dependencies
import pytest
import pandas as pd
import numpy as np
from normtestPY.params_mle import params_mle

# Dummy data for testing in different datatypes
dummy = pd.DataFrame({"var1": [0,1,1,-1], "var2": [-1, -1, 0, 1]})
series_type = (dummy["var1"])
matrix_type = np.array(dummy)
list_2d_type = list([list(dummy["var1"]), list(dummy["var2"])])

# Expected output from Dummy
expected = pd.DataFrame({"var1": [1/4, 11/16], "var2": [-1/4, 11/16]}, index = ["Mean", "Variance"])

# Unit tests
def test_params_mle_calc():
    assert np.allclose(params_mle(dummy), expected)
    assert np.allclose(params_mle(series_type), pd.DataFrame(expected["var1"]))
    assert np.allclose(params_mle(matrix_type), expected)
    assert np.allclose(params_mle(list_2d_type), expected)

def test_output_type():
    assert isinstance(params_mle(dummy), pd.DataFrame)
    assert isinstance(params_mle(matrix_type), pd.DataFrame)
    assert isinstance(params_mle(list_2d_type), pd.DataFrame)
    assert isinstance(params_mle(series_type), pd.DataFrame)

def test_empty_inputs():
    with pytest.raises(ZeroDivisionError):
        params_mle(pd.DataFrame({"var1": [], "var2": []}))
    with pytest.raises(ZeroDivisionError):
        params_mle(list())

def test_non_numeric_inputs():
    with pytest.raises(TypeError):
        params_mle(["male", "female", "male", "female"])
    with pytest.raises(TypeError):
        params_mle(pd.DataFrame({"var1": [1,2,"5","9"]}))
    with pytest.raises(TypeError):
        params_mle([True, False, True])
