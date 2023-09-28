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

# PART 2
flow_5yr=[]
for skipper in flow_data[:,0]:
        if flow_data[:,0] >= 2015 & flow_data[:,0] <= 2019:
              flow_5yr=np.append()

flow_avg = np.mean(flow_5yr[:,3])
print(flow_avg)

# PART 3

flow_daily=[]
flow_daily = flow_avg * 86400    # i thought would be by 2
print(flow_daily(0, 4))

print(np.sum(flow_daily))


# PART 4

flow_monthly = # [][year month flow]     12 x 5 is 60 rows
flow_month = np.zeros(60, 3)
flow_monthly[:, 0] = np.tile(np.arange(2015, 2019, 1),5)


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