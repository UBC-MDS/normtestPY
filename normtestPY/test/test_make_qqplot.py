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
import pytest

from normtestPY.make_qqplot import make_qqplot

# Sample data
data = [1, 2, 3]
data_array = np.array([[1, 2], [3, 4]])
data_array_one = np.array([1,2,3])
data_series = pd.Series({'a':1,'b':2,'c':3})
data_series_named = pd.Series({'a':1,'b':2,'c':3},name='test')
data_df = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]})
data_lists = [[1,2,3],[4,5,6],[7,8,9]]

# Unit tests
def test_output():
    """Check that output is a dict."""
    plots = make_qqplot(data)
    assert type(plots) == dict

def test_bad_inputs_string():
    """Check that an error is thrown from non-numeric inputs"""
    try:
        make_qqplot('a',False)
    except TypeError:
        return True
    raise TypeError

def test_bad_inputs_string_in_list():
    """Check that an error is thrown from non-numeric inputs within a list"""
    try:
        make_qqplot([1,'a',2,'b'],False)
    except TypeError:
        return True
    raise TypeError


def test_bad_inputs_print_plots():
    """Check that an error is thrown from bad inputs to print_plots argument"""
    try:
        make_qqplot(data_df, print_plots='yes')
    except TypeError:
        return True
    raise TypeError


def test_var_length_list():
    """Check that length of dict == 1 when passed list."""
    plots = make_qqplot(data,print_plots=False)
    assert len(plots.keys()) == 1

def test_empty_dataset():
    """Check that length of dict == 1 when passed list."""
    try:
        plots = make_qqplot([],print_plots=False)
    except ValueError:
        return True
    raise TypeError

def test_var_length_list_of_lists():
    """Check that length of dict <= number of lists when passed a list of lists."""
    plots = make_qqplot(data_lists,print_plots=False)
    assert len(plots.keys()) <= len(data_lists)

def test_var_length_array():
    """Check that length of dict <= length of columns in an array when passed an array."""
    plots = make_qqplot(data_array,print_plots=False)
    assert len(plots.keys()) <= data_array.shape[1]

def test_var_length_array_one():
    """Check that length of dict <= length of columns in an array when passed a 1d-array."""
    plots = make_qqplot(data_array_one,print_plots=False)
    assert len(plots.keys()) == 1

def test_var_length_df():
    """Check that length of dict <= length of columns when passed a dataframe."""
    plots = make_qqplot(data_df,print_plots=False)
    assert len(plots.keys()) <= len(data_df.columns)


def test_var_length_series():
    """Check that length of dict == 1 when passed a series."""
    plots = make_qqplot(data_series,print_plots=False)
    assert len(plots.keys()) == 1


def test_var_length_series_named():
    """Check that length of dict == 1 when passed a named series."""
    plots = make_qqplot(data_series_named,print_plots=False)
    assert len(plots.keys()) == 1


def test_plots():
    """Check that each element is a plot"""
    plots = make_qqplot(data,print_plots=False)
    for key in plots.keys():
        assert isinstance(plots[key], matplotlib.figure.Figure)

def test_key_names_array():
    """Check key names for an array-like object"""
    plots = make_qqplot(data_array,print_plots=False)
    for n, key in enumerate(plots.keys()):
        assert n == key


def test_key_names_df():
    """Check key names for a df-like object"""
    plots = make_qqplot(data_df,print_plots=False)
    for key in plots.keys():
        assert key in data_df.columns


