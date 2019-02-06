# normtestPY

Contributors: Constantin Shuster, Sylvia Lee, Richie Zitomer

This is a Python package that tests your data for normality!

### Overview    
A common and important assumption that is made by parametric statistical methods (t-tests, ANOVA and linear regression) is that the dependent variable (response) is normally distributed across all categories of the independent variables (predictors). Thus testing for normality in the data is an important step before applying parametric statistical methods. Graphical and statistical methods can be used to test whether sample data was drawn from a normal population. In normality testing it is important to remember that our null hypothesis is that the sample data is **NOT different** than a normal population with the same mean and variance. If we **fail to reject** this null hypothesis (meaning p-value > 0.05) then we would be able to apply parametric statistical methods to our data. Normality testing can also be used to check whether sample data approximates a normally distributed population. More on this topic can be found [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3693611/) and [here](http://webspace.ship.edu/pgmarr/Geo441/Lectures/Lec%205%20-%20Normality%20Testing.pdf)

This package will test your data for normality using a graphical and a statistical method. As a graphical method, quantile-quantile plots (Q-Q plot) will be constructed in order for you to visualize whether the data closely approximates a straight line - thereby indicating it is normally distributed. As a statistical method, the Shapiro-Wilk test score will be calculated along with the corresponding p-value. The Shapiro-Wilk test provides better power than most other statistical normality tests as long as **most of the values are unique** [<sup>1</sup>](https://www.graphpad.com/guides/prism/7/statistics/index.htm?stat_choosing_a_normality_test.htm). This package will also derive the parameters that would fit your data to a normal distribution using maximum likelihood estimation.

### Package functions:  
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
