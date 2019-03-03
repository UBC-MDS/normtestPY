# Dependencies
import pandas as pd
import numpy as np
from scipy.stats import norm
from math import exp

def shapiro_wilk(data):
    '''
    Conduct the Shapiro-Wilk test for every continuous variable in the data to test for normality.

    Parameters
    ----------
    data : ndarray, dict, pd.DataFrame or pd.Series
        Data to be tested for normality.
        All input data has to be numeric, otherwise TypeError will be raised.
        ndarray will be tested for normality by column.

    Returns
    -------
    shapiro_stats : list
        Test statistics for each continuous variable in the dataframe, by order in which they appear in the dataframe.
        If Shapiro-Wilk statistic evaluates > 1, we set it to 0.9999 to protect the math evaluation of the z-score - data will still be appropriately evaluated as normally distributed.
    p_values : list
        Second list contains the p-values of the test statistics, by order in which they appear in the dataframe

    Examples
    --------
    iris_data = pd.DataFrame({"length": [1,2,3,4], "width": [5,6,7,8])
    shapiro_wilk(iris_data)
    '''

    ## PREPROCESSING
    ## =============

    # Address different input types
    if isinstance(data, np.ndarray):
        if len(data.shape) == 1:
            var_names = [0]
            data = data.reshape(-1,1)
        else:
            n_var = data.shape[1]
            var_names = range(n_var)
    elif isinstance(data, pd.DataFrame):
        n_var = data.shape[1]
        var_names = range(n_var)
        data = np.array(data)
    elif isinstance(data, pd.Series):
        if data.name is not None:
            var_names = [data.name]
        else:
            var_names = [0]
        data = np.array(data)
        data = data[:, None]
    elif isinstance(data, list):
        if type(data[0]) in (float,int):
            var_names = [0]
        else:
            var_names = range(len(data))
        data = np.array(data)
        data = data[:, None]
    else:
        raise TypeError

    # Exception handling if array element is not numeric
    if data.dtype.kind not in ["i", "u", "f", "c"]:
        raise TypeError

    # create lists to be returned
    shapiro_stats = list()
    p_values = list()

    ## Calculations
    ## =============
    ## algorithm reference: http://www.real-statistics.com/tests-normality-and-symmetry/statistical-tests-normality-symmetry/shapiro-wilk-expanded-test/

    for i in var_names:
        x = data[:, i]
        n = len(x)

        # cannot perform shapiro-wilk test if n<=3 or n>5000, raise
        if n <= 3:
            raise ValueError ("Must have greater than 3 observations in each dataset to calculate this statistic")
        elif n > 5000:
            raise ValueError ("Statistic is inaccurate when > 5000 observations. Please split data randomly.")

        #### let W be the Shapiro-Wilk test statistic
        #### W = b^2/SSE

        #### step 1: sort list(x)
        y = sorted(x)

        #### step 2: calculate m[i] values using inverse CDF
        #### mi = inverse CDF of ((i − .375)/(n + .25)), i = 1 to n
        m = np.zeros(n)
        for i in range(len(m)):
            m[i] = norm.ppf((i-0.375+1)/(n+0.25))

        #### step 3: calculate M
        M = np.sum(m**2)

        #### step 4: calculate u
        u = 1/(n**0.5)

        #### step 5: calculate a[i] values
        a = np.zeros(n)
        a[n-1] = -(2.706056*(u**5)) + (4.434685*(u**4)) - (2.071190*(u**3)) - (0.147981*(u**2)) + (0.221157*u) + (m[n-1]*(M**-0.5))
        a[n-2] = -(3.582633*(u**5)) + (5.682633*(u**4)) - (1.752461*(u**3)) - (0.293762*(u**2)) + (0.042981*u) + (m[n-2]*(M**-0.5))
        a[1] = -a[n-2]
        a[0] = -a[n-1]
        e = (M-(2*(m[n-1]**2))-(2*(m[n-2]**2)))/(1-(2*(a[n-1]**2))-(2*(a[n-2]**2)))
        if n > 4:
            for i in range(2 ,n-2):
                a[i] = m[i]/(e**0.5)

        #### step 6: calculate W (Shapiro-Wilk) statistic
        b = np.sum(a*y)
        SSE = np.sum((x-np.mean(x))**2)
        W = (b**2)/SSE

        #### step 7: calculate p-value, knowing that ln(1-W) is approximately normally distirbuted
        mu = 0.0038915*(np.log(n)**3) - 0.083751*(np.log(n)**2) - 0.31082*(np.log(n)) - 1.5861
        exponent = 0.0030302*(np.log(n)**2) - 0.082676*(np.log(n)) - 0.4803
        sd = exp(exponent)

        #### if W >= 1 protect ouput by making W = 0.99
        #### W >=1 means the data is normal in any case so for user won't change outcome
        if W > 1:
            W = 0.9999

        #### calculate z-score and p-value
        p = 1-norm.cdf(np.log(1-W), mu, sd)

        #### append W and p to lists
        shapiro_stats.append(W)
        p_values.append(p)

    return shapiro_stats, p_values
