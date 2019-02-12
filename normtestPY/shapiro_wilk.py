def shapiro_wilk(data):
    '''
    Conduct the Shapiro-Wilk test for every continuous variable in the data to test for normality.

    Parameters
    ----------
    data : ndarray, list, dict, or DataFrame
        Data to be tested for normality

    Returns
    -------
    statistic : list
        Test statistics for each continuous variable in the dataframe, by order in which they appear in the dataframe
    p : list
        Second list contains the p-values of the test statisticas, by order in which they appear in the dataframe

    Examples
    --------
    iris_data = pd.DataFrame({"length": [1,2,3,4], "width": [5,6,7,8])
    make_qqplot(iris_data)
    '''

    print("shapiro_wilk - empty function")

    return()
