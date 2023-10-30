# %%
# EXERCISE 1:
# Write a function that takes the month as input and returns the number of non-leap year days in that month as output


def month(a):
   if a == 4 or a == 6 or a == 9 or a == 11:
    answer = 30
    return(answer)
   elif a == 2:
     return(28)
   else:
     return(31)
   

month(4)      # this is the print statement

#%%
# EXERCISE 2:
# Write a function that takes takes your streamflow dataframe and one other user defined variable as an input and returns some metric of interest


import numpy as np
import pandas as pd
import os
filename = 'streamflow_week8.txt'
filepath = os.path.join('data', filename)  
filepath = '../../data/streamflow_week8.txt'
data = pd.read_table(filepath, sep='\t', skiprows=31,
                     names=['agency_cd, site_no',
                            'datetime', 'flow', 'code'],
                            parse_dates=['datetime'])
df = data.copy()
df = df.set_index('datetime')
df.dropna()


def monthly_max(dataframe, month, year=2019):
    monthly_vals = dataframe[(dataframe.index.month == month) & 
                             (dataframe.index.month == year)]
    maxval=np.max(monthly_vals['flow'])
    return(maxval)
  
monthly_max(df, 5)

#%%
## Exercise 3:
# Write a function to create one of your figures from the previous homework
