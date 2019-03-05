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
        if type(data[0]) in (float,int):
            var_names = [0]
        else:
            var_names = range(len(data))
        data = np.transpose(np.array(data))

    else:
        print("invalid input data type")
        raise TypeError

    # Retrieve size of data
    n_obs = data.shape[0]

    ## Calculations
    ## =============
    np.seterr(divide = "raise", invalid = "raise")

    # Calculate mu estimates
    try:
        mu = np.divide(np.sum(data, axis = 0), n_obs)
        assert(np.any(np.isnan(mu)) == False)
    except:
        print("Warning: Missing values detected in one or more variables")
        mu = np.divide(np.nansum(data, axis = 0), n_obs)

    # Calculate sigma estimates
    variance = np.nansum((data - mu)**2, axis = 0)/n_obs

    ## Return results
    ## ==============
    mle_params = pd.DataFrame(np.vstack((mu, variance)), index = ["Mean", "Variance"], columns = var_names)

    return mle_params

#dummy = pd.DataFrame({"var1": [0,1,1,-1], "var2": [-1, -1, 0, 1]})
#params_mle([[2, 1, 3], [1,2,3,4]])
