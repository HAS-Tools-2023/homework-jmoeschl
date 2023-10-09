#%%
import numpy as np
import pandas as pd

# %%
# Warm Up Exercise 1 (For loop review): 
# Assume you have a numpy array called ‘precip’ that hourly precipitation measurements for one month. The array has three columns[day, hour, precip] and 720 rows(24 hours of data for 30 days). The days numbers are integers which start at 1 and go to 30
# Write a Python Script to calculate the daily total precipitation and save it in an array with two columns called ‘daily’ where the first column is the day and the second column is the daily precipitation. 

#Creating some dummy data for the precip array
precip=np.zeros((720,3))
precip[:,0]=np.repeat(np.arange(1,31),24)
precip[:,1]=np.tile(np.arange(1,25),30)
precip[:,2]=np.random.rand(720)

daily=np.zeros((30,2))
daily[:,0]=np.arange(1,31)
d=1
for i in range(30):
    print(i)
    daily[i,1]=np.sum(precip[(precip[:,0]==d),2])
    d=d+1

np.mean()

# %%
# Pandas Indexing Exercise 1
#data = np.random.randn(7,3)
data = np.ones((7, 3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

#First lets just look at our dataframe
data_frame.info
data_frame.describe

# Exercise 1.1:  Change the values for all of the vowel rows to 3
data_frame.loc[['a','e']] = 3
print(data_frame)


#%% 
# Exercise 1.2: multiply the first 4 rows by 7
data_frame = data_frame.iloc[:4, ] * 7
print(data_frame)

#%% 
# Exercise 1.3:  Make the dataframe into a checkerboard  of 0's and 1's using loc
data_frame2 = data_frame * 0 +1
data_frame2.loc[['a', 'c', 'e', 'g'], ['data1', 'data3']] = 0
data_frame2.loc[['b', 'd', 'f'], ['data2']] = 0

#%%

# Exercise 1.4:  Do the same thing without using iloc
#data_frame3 = data_frame * 0 +1
data_frame3.iloc[0:8:2, 0:3:2] = 0
data_frame3.iloc[1:8:2, 1:3:2] = 0

#_________________________________________________________
# %%
# Pandas Indexing Exercise 2
data_frame = pd.DataFrame([[1, np.nan, 2],
                           [2, 3, 5],
                           [np.nan, 4, 6]])

# Exercise 2.1:  Fill the NA values with 999
data_frame9 = data_frame.fillna(999)

# Exercise 2.2: Turn the 999 values back into NA   
# See if you can come up with 3 different ways to do this

# approach 1
data_frame9 = data_frame.fillna(999)
data_frame9[data_frame9 == 999] = np.nan

# approach 2
data_frame9 = data_frame.fillna(999)
data_frame9[data_frame.isnull()] = np.nan

# approach 3
data_frame9 = data_frame.fillna(999)
data_frame9 = data_frame9 + data_frame
