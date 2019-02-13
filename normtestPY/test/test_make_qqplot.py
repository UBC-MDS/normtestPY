'''
This script tests the function from make_qqplot.py

Parameters
----------
None

Returns
-------
Assertion errors if tests fail
'''
#Dependencies
import numpy as np
import pandas as pd
import matplotlib

from normtestPY.make_qqplot import make_qqplot

# Sample data
data = [1, 2, 3]
data_array = np.array([[1, 2], [3, 4]])
data_series = pd.Series({'a':[1,2,3]})
data_df = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]})

# Unit tests
def test_output():
    """Check that output is a dict."""
    plots = make_qqplot(data)
    assert type(plots) == dict


def test_var_length_list():
    """Check that length of dict == 1 when passed list."""
    plots = make_qqplot(data)
    assert len(plots.keys()) == 1


def test_var_length_array():
    """Check that length of dict <= length of columns in an array when passed an array."""
    plots = make_qqplot(data_array)
    assert len(plots.keys()) <= data_array.shape[1]


def test_var_length_df():
    """Check that length of dict <= length of columns when passed a dataframe."""
    plots = make_qqplot(data_df)
    assert len(plots.keys()) <= len(data_df.columns)


def test_var_length_series():
    """Check that length of dict == 1 when passed a series."""
    plots = make_qqplot(data_series)
    assert len(plots.keys()) == 1


def test_plots():
    """Check that each element is a plot"""
    plots = make_qqplot(data)
    for key in plots.keys():
        assert isinstance(plots[key], matplotlib.figure.Figure)

def test_key_names_array():
    """Check key names for an array-like object"""
    plots = make_qqplot(data_array)
    for n, key in enumerate(plots.keys()):
        assert n == key


def test_key_names_df():
    """Check key names for a df-like object"""
    plots = make_qqplot(data_df)
    for key in plots.keys():
        assert key in data_df.columns
