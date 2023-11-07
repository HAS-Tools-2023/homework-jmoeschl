import numpy as np
import pandas as pd
# %%
# EXERCISE 1:
# Write a function that takes the month as input and returns the number of non-leap year days in that month as output
def days_in_month(month):
    if month==2:
        return(28)
    elif month==4 or month ==6 or month==9 or month ==11:
        return(30)
    elif month>=1 and month<=12:
        return(31)
    else:
        print('Not a valid month please enter an integer between 1 adn 12')
        return(-99)
    
days_in_month(30)


#%%
# EXERCISE 2:
# Write a function that takes takes your streamflow dataframe and one other user defined variable as an input and returns some metric of interest
data = pd.read_table('streamflow_demo.txt', sep='\t', skiprows=30, names=['agency_cd', 'site_no',
                             'datetime', 'flow', 'code'],
                      parse_dates=['datetime']
                     )
datai = data.copy()
datai = datai.set_index('datetime')

def monthly_max(dataframe, month, year=2019):
    monthly_vals = dataframe[(dataframe.index.month ==month)  &(dataframe.index.year == year)]
    maxval=np.max(monthly_vals['flow'])
    print('calculating max for month:', month, 'year', year)
    return(maxval)


monthly_max(datai, 5, 2015)

monthly_max(month=5, year=2020, dataframe=datai)

monthly_max(datai, 5)





#%%
## Exercise 3:
# Write a function to create one of your figures from the previous homework
