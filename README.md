# Normtest

This is a python package that tests for normality in your data!

Functions:
1. make_qqplot()
    - input: dataframe, series, list, or array
    - output: list of plots
2. shapiro_wilk()
    - input: dataframe, series, list, or array
    - output: dataframe
        - columns: variables
        - rows: test statistic, p-value
3. params_mle()
    - input: dataframe, series, list, or array
    - output: dataframe
        - columns: variables
        - rows: mean, variance
        
