#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%

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
data_frame = pd.DataFrame(data,
                        columns=['flow', 'year', 'month', 'day'])

data_frame.dropna()


#%%
###################################################################################################################################################

#%%             PULLING OUT ALL OCTOBER DATA

october_data = data_frame[data["month"]  == 10]

print(october_data)

#%%             ??QUESTION?????

# how do i make it pull out all of october and get the average of each october per year

i = 2000
for i in "year":
    if "month" == 10:
        



# %%            PULLING OUT ALL FLOW BELOW 60 CFS

low_flow_value=data_frame[data["flow"] <= 60]
print(low_flow_value)
low_flow_count=data_frame[data["flow"] <= 60].count()
print(low_flow_count)


#%%             GROUPING FLOWS BY MONTH AND DESCRIBING

flow_by_month=data_frame.groupby(["month"])[["flow"]].describe()
print(flow_by_month)

#%%             INDIVIDUAL STATS (MAX and MIN)

fbm_max=data_frame.groupby(["month"])[["flow"]].max()
print(fbm_max)

fbm_min=data_frame.groupby(["month"])[["flow"]].min()
print(fbm_min)

#%%             INDIVIDUAL STATS (MEAN and STD)

fbm_mean=data_frame.groupby(["month"])[["flow"]].mean()
print(fbm_mean)

fbm_std=data_frame.groupby(["month"])[["flow"]].std()
print(fbm_std)

#%%             GRAPH ONE: for october_data (histogram) YAY IT WORKED

f, ax = plt.subplots()
ax.bar(x=october_data.day, 
        height=october_data.flow, 
        color="purple",
        label='avg flow')
ax.set(title="Average Flow on Each Day of October")
plt.legend(loc='upper right')
plt.show()


#%%             GRAPH TWO: scatter plot of low_flow_value


f, ax = plt.subplots()
ax.scatter(low_flow_value.index, low_flow_value.flow, color="red", label='flow')
ax.set(title="Low Flow Values vs. Day (<= 60 cfs)")
ax.set(xlabel="day number", ylabel="flow (cfs)")
plt.legend(loc='lower right')
plt.show()

#%%   BROKEN    GRAPH TWO: subplots of month max, min, mean, std

fig,ax = plt.subplots(2,2, sharex='col')
ax = ax.flatten()
plt.ylabel("Flow(cfs)")
plt.xlabel("month")
plt.title("Summary of Statistics")
#plt.legend(loc='upper right')

ax[0].scatter(fbm_max.index, fbm_max["flow"], color='red', label='Max')
ax[0].set_title("Max")
ax[1].plot(fbm_min.index, fbm_min["flow"], color='blue', label='Min')
ax[1].set_title("Min")
ax[2].scatter(fbm_mean.index, fbm_mean["flow"], color='yellow', label='Mean')
ax[2].set_title("Mean")
ax[3].scatter(fbm_std.index, fbm_std["flow"], color='green', label='Stdev')
ax[3].set_title("stdev")

plt.legend(loc='upper right')

#%%             GRAPH THREE: ABOVE ANOTHER WAY

fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2,2, sharex='col')
plt.ylabel("Flow(cfs)")
plt.xlabel("month")

ax1.bar(fbm_max.index, fbm_max["flow"], color='red', label='Max')
ax1.set_title("Max")
ax1.legend(loc='upper right')

ax2.scatter(fbm_min.index, fbm_min["flow"], color='blue', label='Min')
ax2.set_title("Min")
ax2.legend(loc='upper right')

ax3.bar(fbm_mean.index, fbm_mean["flow"], color='yellow', label='Mean')
ax3.set_title("Mean")
ax3.legend(loc='upper right')

ax4.bar(fbm_std.index, fbm_std["flow"], color='green', label='Stdev')
ax4.set_title("Stdev")
ax4.legend(loc='upper right')



#%%             GRAPH FOUR: min flow of each month as a quadratic (compared to the plain max)

f, ax = plt.subplots(1,1)
plt.title("Min Per Month Squared Against Monthly Max")
plt.xlabel("Month")
plt.ylabel("Flow (cfs)")

ax.plot(fbm_min.index , fbm_min**2, color='blue', label='min squared')
ax.plot(fbm_max.index, fbm_max["flow"], color='red', label='max')
ax.legend(loc='upper right')



#%%             GRAPH FIVE: density plot of october_data 


plt.hexbin(october_data.index, october_data.flow, gridsize=100, cmap='Blues')
plt.xlabel('day number')
plt.ylabel('flow')
plt.ylim(0, 500)
plt.title('Density of October Flows')
cb = plt.colorbar(label='flow count')



# %%            MY QUESTIONS

QUESTIONS!!
1. how do i make october_data show me its max and min
2. for the describing and grouping, how do i get it to do max per month pulled out
   

