import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_qqplot(data, print_plots = True):
    '''
    Create QQ-plot for each continuous variable in the data

    Parameters
    -------
    data : ndarray, list, dict, or DataFrame
        Data to be tested for normality. ALL data must be numeric or the
        function will raise a TypeError.

    print_plots: Boolean
        Toggle whether or not the plots are interactively printed out while
        they're being created. Default is True.

    Returns
    -------
    plots : dict
        Dictionary of plots where the keys are the column name (or index)

    Examples
    -------
    iris_data = pd.DataFrame({"length": [1,2,3,4], "width": [5,6,7,8])
    make_qqplot(iris_data)
    '''

    # Address different input types
    if isinstance(data, np.ndarray):
        if len(data.shape) == 1:
            var_names = [0]
            data = data[:, None]
        else:
            n_var = data.shape[1]
            var_names = range(n_var)

    elif isinstance(data, pd.DataFrame):
        var_names = list(data)
        data = np.array(data)

    elif isinstance(data, pd.Series):
        if data.name is not None:
            var_names = [data.name]
        else:
            var_names = [0]
        data = np.array(data)
        data = data[:, None]

    elif isinstance(data, list):
        try:
            assert len(data) > 0
        except AssertionError:
            raise ValueError("ERROR: Empty dataset")
        if type(data[0]) in (float,int):
            var_names = [0]
        else:
            var_names = range(len(data))
        data = np.transpose(np.array(data))
        data = data[:,None]

    else:
        raise TypeError("ERROR: invalid input data type")


    # Exception handling if array element is not numeric
    if data.dtype.kind not in ["i", "u", "f", "c"]:
        raise TypeError

    q = np.linspace(0,1,20) # Sequence of quantiles
    x = np.quantile(np.random.normal(0, 1, 1000), q)  # Get a thousand observations for a theoretical dist

    plots = {}
    for n,column in enumerate(data.T):
        y = np.quantile(column, q)
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        plt.xlabel('Theoretical Distribution')
        plt.ylabel('Sample Distribution')
        try:
            assert type(print_plots) == bool
        except AssertionError:
            raise TypeError('ERROR: need to specify a boolean for print_plots')
        if print_plots:
            plt.show()
        else:
            plt.close()
        plots[var_names[n]] = fig

    return plots

