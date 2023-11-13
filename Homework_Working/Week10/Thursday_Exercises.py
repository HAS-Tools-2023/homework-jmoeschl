## Exercises for thursday's class
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%

# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 

#MINE:

data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=31, 
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                            index_col=['datetime'],
                            parse_dates=['datetime'])

#%%
#DR CONDONS:
data_datetime = pd.read_table('streamflow_demo.txt'
sep='\t', skiprows=31, names=['agency_cd', 'site_no', 
                              'datetime', 'flow', 'code'],
                parse_dates=['datetime'], index_col='datetime')



#%%
# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 

#MINE
columns=['date', 'year', 'yday', 'dayL (s)', 'prcp (mm/day)','srad (W/m^2)', 
       'swe (kg/m^2)', 'tmax (deg c)',	
       'tmin (deg c)','vp (Pa)']
datatwo = pd.read_csv('daymet.csv',  
                     parse_dates=['date'], index_col=['date'])

#%%
#DR CONDONS:
daymet_df = pd.read_csv('daymet.csv', parse_dates=['date'], index_col=['date'])

#%%

#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 
#MINE
print(datatwo.describe())
datatwo.info()

#%%
# using daymet_df

daymet_df.info()

#%%
#2.3  Make a scatter plot of day length (dayl) vs maximum temperature. Fit a trend line 

#ax = plt.axes()

fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.scatter(datatwo['dayL (s)'], datatwo['tmax (deg c)'],
                color='blue')
#%%
fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.scatter(datatwo.index, datatwo['tmax (deg c)'],
                color='green')



#%%
#2.4 Make a plot with three lines (1) average, (2) min and (3) max shortwave radiation (srad) vs the day of the year (i.e. 1-365)
# MY CALCS
doymax=datatwo.groupby('yday').max()
doymin=datatwo.groupby('yday').min()

#%%
#datatwo['yday'] = pd.to_numeric(datatwo['yday'], downcast='float')

doyavg=datatwo.groupby('yday').mean()



#%%
# MY PLOTS
plt.plot(doymax.index, doymax['srad (W/m^2)'], color='red')
plt.plot(doymin.index, doymin['srad (W/m^2)'], color='yellow')

#%%
plt.plot(doyavg.index, doyavg['srad (W/m^2)'], color='purple', xaxis='day',
         yaxis='srad', title='srad avg')


#%%
# FROM CLASS

fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.plot(datatwo['yday'], doymax['srad (W/m^2)'],
                color='red')
fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.plot(datatwo['yday'], datatwo['srad (W/m^2)'],
                color='yellow')
fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.plot(datatwo['yday'], datatwo['srad (W/m^2)'],
                color='purple')

# %%  other 2.4

#2.4 Make a plot with lines for the monthly average of `tmax` for all months after Jan 2015.  Add shading to the plot extending to the monthly minimum and maximum of `tmax` for the same period.

#Hint - Use the pandas resample function for datetime objects and the plt.fill type for the shading. 

FROM TONG:

daymet_after_2015= datatwo[datatwo.index.year >= 2015]
daymet_after_2015_monthly = daymet_after_2015.resample('M')['srad (W/m^2)']
srad_mean=daymet_after_2015_monthly.mean()
srad_min=daymet_after_2015_monthly.min()
srad_max=daymet_after_2015_monthly.max()
ax = plt.axes()
ax.plot(srad_mean, '-', color='blue',label='mean srad')
ax.plot(srad_max,'--',color='orange',label='max srad')
ax.plot(srad_min, ':', color='green',label='min srad' )
ax.set(xlabel='month of every year after 2015', ylabel='srad value')
ax.legend()  
