# Starter code for week 6 Pandas

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week2.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week2.txt'


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


#%%

# making my data frame

data_frame = pd.DataFrame(data,
                        columns=['flow', 'year', 'month', 'day'])



#%%
# see if it worked

data_frame.describe



#%%
# get rid of bad data

data_frame.dropna()



#%%

## trying to find what the flow is stored as so i can pick values out


data_frame.loc[:, 'flow']



#%%

## trying to make a plot:              ** BROKEN PART **

data_frame.plot.bar(['day', 'flow'])





#%%

# stats before october

print(data_frame.max())         # 42200
print(data_frame.min())         # 19
print(data_frame.mean())        # 319
print(data_frame.std())         # 1161
print(data_frame['flow'].quantile([0.25, 0.5, 0.75]))   # 87, 147, 207



#%%

data.sort_values(by="flow", ascending = True)
print(data[['datetime', 'month', 'flow']].head(5))
print(data[['datetime', 'month', 'flow']].tail(5))


# why not dataframe.head


#%%
# I DONT GET THIS PART

# 5. provide a list of historical dates with flows that are within 10% of your
# week 1 forecast value. If there are none than increase the %10 window until 
# you have at least one other  value and repor the date and the new window you used
forecast = 72
window = 0.10

#Filter for days that fall within this window: 
window_days = data[(data['flow']> forecast*(1-window)) & 
      (data['flow'] <  forecast * (1+window)) &
      (data['month'] ==9)]

window_days['datetime']

#same thing on one line:
data[(data['flow'] > forecast*(1-window)) &
                   (data['flow'] < forecast * (1+window)) &
                   (data['month'] == 9)]['datetime']




#%%

## tryign to separate the month of 10 

october=data_frame.loc[data['month'] == 10]


#%%

# finding the average and maximum and minimum of october

print(october.mean())                   # 144.8
print(october.max())                    # 1910
print(october.min())                    # 59.8
print(october.std())                    # 131.8
print(october['flow'].quantile([0.25, 0.5, 0.75]))      # 101, 119, 146


########## works to this point ########### (gets the assignemtn done too)



#%% 

## trying to get the day in specific

# not working (these are ideas)

data_frame.loc[data(['month'] == 10) & (['day'] == 15)]

data.loc[data_frame(['month'] == 10) & (['day'] == 15)]





# %%
# Warm up exercises: 

# %%
# 1. How do you see a quick summary of what is in `data`?

        # Using the expansion of the Jupyter Variable feature
data_frame.describe


# %%
# 2. How do you get a listing of the columns in `data`?

data_frame.columns


# %%
# 3. How do you select the streamflow column in `data`?

print(data_frame.loc[:, 'flow'])


#%%
# 5. How do you get the last streamflow value from `data`?

print(data_frame.tail(1))


#%%
# 6. What is the mean streamflow value for entire period?

319 cfs


#%%
# 7. What is the maximum value for the entire period?

42200 cfs 


#%%
# 8. How do you find the maximum streamflow value for each year?

year=data_frame.loc[data['year'] == 2000]  # change for each year
print(year.max())


