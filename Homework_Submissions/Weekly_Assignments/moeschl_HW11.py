#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# %%

filename = 'streamflow_week8.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../../data/streamflow_week8.txt'

data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

data_frame = pd.DataFrame(data,
                        columns=['flow', 'year', 'month', 'day'])

data_frame.dropna()

#%%     NOVEMBER DATA FRAMES

#all of november data with day and years        one average value for all of november
november = data_frame[data["month"] == 11]
november_data = november.mean()

#%%     NOVEMBER GRAPH

f, ax = plt.subplots()              # making a graph of thr maximum flows per day in november
ax.bar(x=november.day, 
        height=november.flow, 
        color="orange",
        label='max flow')
ax.set(title="Max Flow on Each Day of November")
plt.legend(loc='upper right')
plt.show()
#%%     GROUPING AND DESCRIBING

# all of the statistics per month for the entire time
flow_by_month=data_frame.groupby(["month"])["flow"].describe()
print(flow_by_month)                    

#%%     MULTI PANEL GRAPH

fig,ax = plt.subplots(2,2, sharex='col')        # 2 by 2 workspace witha  shared x axis
ax = ax.flatten()
plt.ylabel("Flow(cfs)")
plt.xlabel("month")
plt.title("Summary of Statistics")

ax[0].scatter(flow_by_month.index, flow_by_month["max"], color='red', label='Max')
ax[0].set_title("Max")          # scatter plot of each months maximum flow
ax[1].plot(flow_by_month.index, flow_by_month["min"], color='blue', label='Min')
ax[1].set_title("Min")          # line (not linear) graph of minimum per month
ax[2].scatter(flow_by_month.index, flow_by_month["mean"], color='yellow', label='Mean')
ax[2].set_title("Mean")         # scatter plot of each months average
ax[3].scatter(flow_by_month.index, flow_by_month["50%"], color='green', label='Median')
ax[3].set_title("Median")       # scatter plot of each months median value

plt.legend(loc='upper right')
 


#%%     FLOW COLUMN PULLED OUT (FOR FORECAST) 
#all of the november data rows for only the flow column
november_flow = november[["flow"]]

#%%     ONE WEEK FORECAST VARIABLE

onewkcalc = (november_flow.std())/(november_flow.mean())
# chose to divide in this order to get the lowest of the options
oneweek = onewkcalc * november_flow.std()

#%%     TWO WEEK FORECAST VARIABLE

twowkcalc = (november_flow.mean())/(november_flow.std())
# lowest value when dividing in this order
twoweek = twowkcalc * november_flow.mean() 


#%%     PRINT STATEMENTS

print("1 week forecast = ", oneweek[0])
print("2 week forecast = ", twoweek[0])