# normtestPY

This is a python package that tests for normality in your data!

Functions:
1. make_qqplot()
    - **description:** this function will read in data and will create a QQ-plot for each continuous variable in the data. It will output a dictionary of plot objects and print them to screen as default (the user will have the option of not printing plots).
    - **input:** dataframe, series, list, or array
    - **output:** list of plots
2. shapiro_wilk()
    - **description:** this function will read in data and will output the shapiro-wilks test for normality for each continuous variable in the data. The output will be a dataframe with one row for the test statistic and one row for the p-value with the columns presenting the original variables in the data.  
    - **input:** dataframe, series, list, or array
    - **output:** dataframe
        - columns: variables
        - rows: test statistic, p-value
3. params_mle()
    - **description:** this function will read in data and will output the mean and variance for the empirical distribution of the data given that the data is normal for each continuous variable in the data. The output will be a dataframe with one row for the mean and one row for the variance with the columns presenting the original variables in the data. 
    - **input:** dataframe, series, list, or array
    - **output:** dataframe
        - columns: variables
        - rows: mean, variance
        
