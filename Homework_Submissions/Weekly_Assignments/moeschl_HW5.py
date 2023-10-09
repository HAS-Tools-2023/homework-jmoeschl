# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%

filename = 'streamflow_week2.txt'
filepath = os.path.join(filename)
print(os.getcwd())
print(filepath)

#%%

data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)


#%% 
#           MY FINAL TRY

picklist = (flow_data[:,0] >= 2015) & (flow_data[:,0] <= 2019)
flow_5yr = flow_data[picklist, :]

#%%

# PART 2
flow_test=np.zeros((1826, 4))
i=0
j=0
for skipper in flow_data[:,0]:          #skipper becomes flow_data year
        if (skipper >= 2015) & (skipper <= 2019):
              flow_test[i,:]=flow_data[j,:]
              i = i+1
        j=j+1


flow_avg = np.mean(flow_5yr[:,3])
print(flow_avg)


#%% PART 3

flow_daily = flow_5yr[:, 3] * 86400    
print(flow_daily[0: 4])

print(np.sum(flow_daily))


#%% PART 4

flow_month = np.zeros((60, 3))
year = np.repeat(np.arange(2015, 2020), 12)
month = np.tile(np.arange(1, 13), 5)

flow_month[:, 0]=year
flow_month[:, 1]=month

for i in range(60):         # i is going 0 to 59
       y_temp = flow_month[i, 0]
       m_temp = flow_month[i, 1]
       picklist = (flow_5yr[:,0] == y_temp) & (flow_5yr[:,1] == m_temp)
       flow_month[i, 2] = np.mean(flow_5yr[picklist, 3])            #picklist is rows
# can do a list of true falses and hold the trues
       
       print(i, y_temp, m_temp, flow_month[i, 2])

#flow_monthly[:, 0] = np.tile(np.arange(2015, 2019, 1),5)


####        QUESTION:
                # HOW DO I GET VARIABLES TO HAVE THE YEAR MONTH FLOW NAMES



#%%


#       FROM CLASS

#if flow_data[:3] >= 2015 & flow_data[:3] <= 2019:
 #   test[:,3] * 86400

#flow = []
#for i in range(len(test[:,1]):
    #temp = test[i:3]*86400
    #flow = np.append(flow, temp)

# %%

# flow_5yr = [year month day flow]  365 x 5 rows
# flow_monthly = [year month flow]  12 x 5 = 60 rows
    # flow_month = np.zeros(60, 3)
    # flow_monthly[:, 0] = np.tile(np.arange(2015, 2019, 1),5)

# for i in range(60):    or range(len(flow_mon[:, 1]))
    # ytemp = flow_monthly[i, 0]
    # mtemp = flow_month[i, 1]
    # print(ytemp, mtemp)
    # ilist = flow_5yr[:, 0] == ytemp & flow_5yr[:, 1] == mtemp
        # flow_5yr[:,1] == mtemp
    #np.mean(flow_5yr[ilist,3])