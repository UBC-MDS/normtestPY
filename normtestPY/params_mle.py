# Dependencies
import pandas as pd
import numpy as np

def params_mle(data):
    '''
    Fit data to a Guassian distribution with Maximum Likelihood Estimation (MLE)

    Parameters
    ----------
    data : ndarray, list, dict, or DataFrame
        Data to be tested for normality

    Returns
    -------
    mle_params : Dataframe
        Dataframe with the first row containing the estimated means and
        the second row containing the estimated variance. The columns
        present the original variables in the data

    Examples
    --------
    iris_data = pd.DataFrame({"length": [1,2,3,4], "width": [5,6,7,8])
    params_mle(iris_data)
    '''

## PREPROCESSING
## =============

    # Address different input types

    if isinstance(data, np.ndarray):
        if len(data.shape) == 1:
            var_names = [0]
        else:
            var_names = range(data.shape[1])
        data = data[:,None]

    elif isinstance(data, pd.DataFrame):
        var_names = list(data)
        data = np.array(data)

    elif isinstance(data, pd.Series):
        if data.name is not None:
            var_names = [data.name]
        else:
            var_names = [0]
        data = np.array(data)

    elif isinstance(data, list):
        if len(data) != 0:
            if type(data[0]) in (float,int):
                var_names = [0]
            else:
                var_names = range(len(data))
        data = np.transpose(np.array(data))

    else:
        print("ERROR: invalid input data type")
        raise TypeError("Invalid input ype")

    # Retrieve size of data
    n_obs = data.shape[0]

    ## Exception handling
    ## ==================
    try:
        assert data.dtype.kind in ["i", "u", "f", "c"]
    except:
        print("ERROR: Incorrect data type; data is not numeric. \nCheck for string and booleans in data; uneven number \nof values in variable lists")
        raise

    ## Calculations
    ## =============
    np.seterr(divide = "raise", invalid = "raise")

    # Calculate mu estimates
    try:
        mu = np.divide(np.sum(data, axis = 0), n_obs)
        assert np.any(np.isnan(mu)) == False

    except AssertionError:
        print("WARNING: Missing values detected in one or more variables")
        mu = np.divide(np.nansum(data, axis = 0), n_obs)
    except FloatingPointError:
        print("ERROR: Division by 0; input data list may be empty")
        raise
    except TypeError:
        print("ERROR: Data is not numeric")

    # Calculate sigma estimates
    variance = np.nansum((data - mu)**2, axis = 0)/n_obs
    assert np.all(variance >= 0)

    ## Return results
    ## ==============
    mle_params = pd.DataFrame(np.vstack((mu, variance)), index = ["Mean", "Variance"], columns = var_names)

    return mle_params
params_mle("hi")
