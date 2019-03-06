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
data_df = pd.DataFrame({'data' : [41.5,38.7,44.5,43.8,46.0,39.4, 40.6, 42.7],
              'data2' : [65,63,86,70,74,35,68,45]})
data_list1 = [41.5,38.7,44.5,43.8,46.0,39.4, 40.6, 42.7]
data_list2 = [1, 2, 3, 4, 5,6,7,8]
data_list3 = [data_list1, data_list2]
data_list4 = [1, 2, 3]
data_ndarray = np.array([[41.5,38.7,44.5,43.8,46.0,39.4, 40.6, 42.7],
                      [65,63,86,70,74,35,68,45]]).T
data_series1 = pd.Series([41.5,38.7,44.5,43.8,46.0])
data_series2 = (data_df['data'])
data_meaningless1 = pd.DataFrame({'a': ["ab", "cd", "ef", "hlp"]})
data_meaningless2 = pd.DataFrame({'b': [True, False, True, False]})
data_meaningless3 = "hopefully this throws a TypeError"

# Unit Tests
def test_output_and_input_type():
    """Check that output is a tuple for all possible inputs"""
    assert type(shapiro_wilk(data_df)) == tuple
    assert type(shapiro_wilk(data_list1)) == tuple
    assert type(shapiro_wilk(data_list2)) == tuple
    assert type(shapiro_wilk(data_list3)) == tuple
    assert type(shapiro_wilk(data_ndarray)) == tuple
    assert type(shapiro_wilk(data_ndarray[:,0])) == tuple
    assert type(shapiro_wilk(data_series1)) == tuple
    assert type(shapiro_wilk(data_series2)) == tuple

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
    stats = shapiro_wilk(data_list2)
    assert len(stats[0]) == len(stats[1])

def test_meaningless_input():
    """check that meaningless input isn't prcoessed"""
    with pytest.raises(TypeError):
        shapiro_wilk(data_meaningless1)
    with pytest.raises(TypeError):
        shapiro_wilk(data_meaningless2)
    with pytest.raises(TypeError):
        shapiro_wilk(data_meaningless3)

def test_wrong_range():
    small_list = np.random.normal(5, 2, 3)
    large_list = np.random.normal(5, 2, 6000)
    with pytest.raises(ValueError):
        shapiro_wilk(small_list)
    with pytest.raises(ValueError):
        shapiro_wilk(large_list)

def calculation_test():
    """check that the shapiro-wilk test statistic is correctly calculated because p-value should be > 0.05"""
    norm_values = np.random.normal(5, 2, 100)
    assert shapiro_wilk(norm_values)[1] > 0.05
