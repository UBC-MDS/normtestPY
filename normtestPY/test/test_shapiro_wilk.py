'''
This script tests the function from shapiro_wilk.py

This function conducts the Shapiro-Wilk test for every continuous
variable in the data
Input:  DATAFRAME where data for each continous variable is in its
        respective column
Output: LISTS where the first list contains the test statistics and the
        second list contains the p-values in the order of the continuous
        variables in the dataframe
'''

import pytest
from normtestPY.shapiro_wilk import shapiro_wilk

# Unit Tests
