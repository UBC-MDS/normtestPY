# normtestPY

Contributors: Constantin Shuster, Sylvia Lee, Richie Zitomer

This is a Python package that tests your data for normality!

### Overview    
A common and important assumption that is made by many (and commonly used) parametric statistical methods (t-tests, ANOVA and linear regression) is that the dependent variable (response variable) is normally distributed across all categories of the independent variables (predictors). Thus testing for normality in the data is an important step before applying parametric statistical methods.

Graphical and statistical methods can be used to test whether sample data was drawn from a normal population. In normality testing it is important to remember that our null hypothesis is that the sample data is **NOT different** than a normal population with the same mean and variance. If we **fail to reject** this null hypothesis - meaning resultant p-value is > 0.05 - then we would be able to apply the appropriate parametric statistical methods to our data. Normality testing can also be used to check whether any sample data approximates a normally distributed population. More on this topic can be found [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3693611/) and [here](http://webspace.ship.edu/pgmarr/Geo441/Lectures/Lec%205%20-%20Normality%20Testing.pdf).

This package will test your data for normality using a graphical and a statistical method. As a graphical method, quantile-quantile plots (Q-Q plot) will be constructed in order for you to visualize whether the data closely approximates a straight line - thereby indicating it is normally distributed. As a statistical method, the Shapiro-Wilk test score will be calculated along with the corresponding p-value. The Shapiro-Wilk test provides better power than most other statistical normality tests, as long as **most of the values are unique** [<sup>1</sup>](https://www.graphpad.com/guides/prism/7/statistics/index.htm?stat_choosing_a_normality_test.htm). This package will also derive the parameters that would fit your data to a normal distribution using maximum likelihood estimation.

### Package functions:  
1. `make_qqplot()`
    - **description:** this function will read in data and will create a QQ-plot for each continuous variable in the data. It will output a dictionary of plot objects and print them to screen as default (the user will have the option of not printing plots).
    - **input:** dataframe, series, list, or array
    - **output:** dictionary of plots, where the keys are the column name (or column index in the case of an array-like object)
2. `shapiro_wilk()`
    - **description:** this function will read in data and will output the shapiro-wilks test of normality for each continuous variable in the data. The output will be  tuple of lists where the first list contains the test statistics in the order of the variables in the input dataframe and the second list contains the p-values in the same respective ordering.   
    - **input:** dataframe, series, list, or array
    - **output:** tuple of lists
        - first list: test statistic
        - second list: p-value
3. `params_mle()`
    - **description:** this function will read in data and will output the mean and variance for the empirical distribution of the data given that the data is normal for each continuous variable in the data. The output will be a dataframe with one row for the mean and one row for the variance with the columns presenting the original variables in the data.
    - **input:** dataframe, series, list, or array
    - **output:** dataframe
        - columns: variables
        - rows: mean, variance

### Where does this fit into the Python ecosystem

The `SciPy.stats` package has a Shapiro-Wilk test function named [`shapiro()`](https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.shapiro.html), it takes in an array of sample data and returns the test statistic as a float and the p-value as a float - both are returned as a tuple. For Q-Q plots in python, there is a package named `statsmodels` and within it - [`statsmodels.graphics.gofplots.qqplot()`](https://www.statsmodels.org/dev/generated/statsmodels.graphics.gofplots.qqplot.html) - there is a function that takes in 1D array data and creates a `matplotlib` figure. It seems that there is no official PIP or Conda package that provides MLE estimation as a standalone method. In the present, MLE operation will require users to write a self-defined function with the help of [`optimize.minimize()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) from `SciPy`.

Two functions from this `normtestPY` package could be found in other python packages, while the `params_mle()` function does not seem to have an official substitute. 'normtestPY' may fit into the Python ecosystem by providing convenience to statisticians whom often need to deal with normality assumptions and estimations. This package is designed to eliminate the hassle to import functions from different packages in which the users may or may not have. 
