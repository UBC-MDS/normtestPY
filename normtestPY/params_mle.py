# Dependencies
import pandas as pd
import numpy as np

def params_mle(data):
    '''
    Fit data to a Guassian distribution with Maximum Likelihood Estimation (MLE)

    Parameters
    ----------
    DATAFRAME where data for each continous variable is in its
              respective column

    Returns
    -------
    DATAFRAME where the first row contains the estimated means and
              the second row contains the estimated variance, and the columns
              present the original variables in the data

    Examples
    --------
    '''

## PREPROCESSING
    ## =============

    # Set default column names as indexes
    try: # 2D data
        n_var = data.shape[1]
        var_names = range(n_var)
    except: # 1D data
        var_names = [0]

    # Address different input types
    if isinstance(data, pd.DataFrame):
        var_names = list(data)
        data = np.array(data)

    elif isinstance(data, pd.Series):
        if data.name != None:
            var_names = [data.name]
        data = np.array(data)

    elif isinstance(data, list):
        var_names = range(len(data))
        data = np.transpose(np.array(data))

    # Retrieve size of data
    n_obs = data.shape[0]

    ## Calculations
    ## =============

    # Calculate mu estimates
    mu = np.sum(np.array(data), axis = 0)/n_obs

    # Calculate sigma estimates
    variance = np.sum((data - mu)**2, axis = 0)/n_obs
    sigma = variance**(1/2)

    ## Return results
    ## ==============
    mle_params = pd.DataFrame(np.vstack((mu, variance)), index = ["Mean", "Variance"], columns = var_names)
    return(mle_params)
