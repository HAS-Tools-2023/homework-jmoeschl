#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%

filename = 'streamflow_week2.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week8.txt'


#%%

data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


#%%     TIME SERIES READ IN (NOT WORKING)

#data2 = pd.read_table(filename, sep='\t', skiprows=31,
#                      names = ['agency_cd', 'site_no',
#                               'datetime', 'flow', 'code'],
#                               parse_dates = ['datetime'])


# %%

data_frame = pd.DataFrame(data,
                        columns=['flow', 'year', 'month', 'day'])

data_frame.dropna()

#%%     OCTOBER AND NOVEMBER DATA FRAMES

october = data_frame[data["month"]  == 10]      #all of october data with day and years
october_data = october.mean()                   #one average value for all of october

#print(october_data)

november = data_frame[data["month"] == 11]
november_data = november.mean()

#print(november_data)

#%%     OCTOBER GRAPH

f, ax = plt.subplots()
ax.bar(x=october.day, 
        height=october.flow, 
        color="purple",
        label='max flow')
ax.set(title="Max Flow on Each Day of October")
plt.legend(loc='upper right')
plt.show()

#%%     NOVEMBER GRAPH

f, ax = plt.subplots()
ax.bar(x=november.day, 
        height=november.flow, 
        color="orange",
        label='max flow')
ax.set(title="Max Flow on Each Day of November")
plt.legend(loc='upper right')
plt.show()
#%%     GROUPING AND DESCRIBING

flow_by_month=data_frame.groupby(["month"])["flow"].describe()
print(flow_by_month)

#%%     MULTI GRAPH

fig,ax = plt.subplots(2,2, sharex='col')
ax = ax.flatten()
plt.ylabel("Flow(cfs)")
plt.xlabel("month")
plt.title("Summary of Statistics")

ax[0].scatter(flow_by_month.index, flow_by_month["max"], color='red', label='Max')
ax[0].set_title("Max")
ax[1].plot(flow_by_month.index, flow_by_month["min"], color='blue', label='Min')
ax[1].set_title("Min")
ax[2].scatter(flow_by_month.index, flow_by_month["mean"], color='yellow', label='Mean')
ax[2].set_title("Mean")
ax[3].scatter(flow_by_month.index, flow_by_month["50%"], color='green', label='Median')
ax[3].set_title("Median")

plt.legend(loc='upper right')
 


#%%     FLOW COLUMN PULLED OUT  

october_flow = october[["flow"]]           #all of the october data rows for only the flow column
november_flow = november[["flow"]]

#%%     ONE WEEK FORECAST VARIABLE

onewkcalc = (october_flow.std())/(october_flow.mean())

oneweek = onewkcalc * october_flow.std()

#%%     TWO WEEK FORECAST VARIABLE

twowkcalc = (november_flow.mean())/(november_flow.std())

twoweek = twowkcalc * november_flow.mean() 


#%%     PRINT STATEMENTS

print("1 week forecast = ", oneweek[0])
print("2 week forecast = ", twoweek[0])


# %%
