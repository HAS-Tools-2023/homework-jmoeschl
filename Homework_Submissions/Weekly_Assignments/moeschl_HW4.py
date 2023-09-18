#%%

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'streamflow_week2.txt'
filepath = os.path.join(filename)
print(os.getcwd())
print(filepath)

import pandas as pd

data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

flow_data = data[['year', 'month','day', 'flow']].to_numpy()

print(np.size(flow_data))
print(np.shape(flow_data))
print(np.ndim(flow_data))

del(data)

# %%
# Count the number of values with flow(3) > 100 and month(1) ==9
import numpy as np

flow_count = np.sum((flow_data[:,3] > 100) & (flow_data[:,1]==9) & (flow_data[:,2] > 15))

criteria = (flow_data[:, 3] > 100) & (flow_data[:, 1] == 9) & (flow_data[:,2] > 15)
pick_data = flow_data[criteria, 3]
flow_mean = np.nanmean(pick_data)

flow_mean = np.nanmean(flow_data[(flow_data[:,3] > 100) & (flow_data[:,1]==9) & (flow_data[:,2] > 15),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")


# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

flow_quants1 = np.nanquantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.nanquantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])

 #%%

 
