'''
This script tests the function from shapiro_wilk.py

Parameters
----------
None

Returns
-------
Assertion errors if tests fail
'''

# dependencies
import pytest
import numpy as np
import pandas as pd
from normtestPY.shapiro_wilk import shapiro_wilk

# Sample data
data = [1, 2, 3]
data_df = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]})
data_meaningless1 = pd.DataFrame({'a': ["ab", "cd", "ef"]})
data_meaningless2 = pd.DataFrame({'b': ["TRUE", "FALSE", "TRUE"]})

# Unit Tests
def test_output_type():
    """Check that output is a tuple"""
    stats = shapiro_wilk(data_df)
    assert type(stats) == tuple


def test_output_tuple_length():
    """check that length of output is two since the tuple always has 2 lists in it"""
    stats = shapiro_wilk(data_df)
    assert len(stats) == 2


def test_output_list_length():
    """check that the length of the first list is as <= amount of columns in pd.dataframe"""
    stats_1 = shapiro_wilk(data_df)[0]
    assert len(stats_1) <= data_df.shape[1]

def test_output_lists_equal():
    """check that the length of the first list is equal to the output of the second list"""
    stats = shapiro_wilk(data)
    assert len(stats[0]) == len(stats[1])

def test_meaningless_input():
    """check that meaningless input isn't prcoessed"""
    with pytest.raises(TypeError):
        shapiro_wilk(data_meaningless1)
    with pytest.raises(TypeError):
        shapiro_wilk(data_meaningless2)

def calculation_test():
    """check that the shapiro-wilk test statistic is correctly calculated because p-value should be > 0.05"""
    norm_values = np.random.normal(5, 2, 100)
    assert shapiro_wilk(norm_values)[1] > 0.05
