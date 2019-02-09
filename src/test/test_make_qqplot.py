import numpy as np
import pandas as pd

from make_qqplot import make_qqplot

data = [1, 2, 3]
data_array = np.array([[1, 2], [3, 4]])
data_series = pd.Series({'a':[1,2,3]})
data_df = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]})
output = {'a': 1, 'b': 2}


def test_output():
    """Check that output is a dict."""
    plots = make_qqplot(data)
    assert type(plots) == dict


def test_var_length_list():
    """Check that length of dict == continuous vars (<=) for a list."""
    plots = make_qqplot(data)
    assert len(plots.keys()) <= len(data)


def test_var_length_array():
    """Check that length of dict == continuous vars (<=)"""
    plots = make_qqplot(data_array)
    assert len(plots.keys()) <= data_array.shape[1]


def test_var_length_df():
    """Check that length of dict == continuous vars (<=)"""
    plots = make_qqplot(data)
    assert len(plots.keys()) <= len(data_df.columns)


def test_plots():
    """Check that each element is a plot"""
    plots = make_qqplot(data)
    for key in plots.keys():
        assert key == 1 # replace with matplot figure


def test_key_names_array():
    """Check key names"""
    plots = make_qqplot(data_array)
    for n, key in enumerate(plots.keys()):
        assert n == key


def test_key_names_df():
    """Check key names"""
    plots = make_qqplot(data_df)
    for key in enumerate(plots.keys()):
        assert key in data_df.columns


def test_plots_range():
    """Check plot x and y range."""
    #plots =


def test_plot_elements():
    """Check elements of plot."""
    pass


# Check that plot if printed
# Check that it is a qqplot?