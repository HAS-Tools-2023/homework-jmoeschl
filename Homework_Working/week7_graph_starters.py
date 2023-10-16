#%%


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%%
## Import the flow data to use
data = pd.read_table("./streamflow_demo.txt", sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


#%%
## Plot 1: Simple line plot
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
y1=np.cos(x)
y2=np.log(x)
y3=x**10
y4=x**2

ax = plt.axes()
plt.style.use('dark_background')
ax.set_title("Sines and Cosines")
ax.plot(x, y1, linestyle='--', label='sinx')
ax.plot(x, y2, label='cosx')
ax.legend(loc='upper right')
ax.plot(x, y1, color="green")
ax.plot(x, y1, linestyle="--")
ax.plot(x, y2, color="pink")
ax.set_xlabel("the x axis")
ax.set_ylabel("the y axis")
plt.plot(x , y4, label='quadratic')
#plt.scatter(x, y3, label='scatter')




#%%
## Plot 2: Scatter Plot
ax=data.plot.scatter(x='month', y='flow',
                     c='year', colormap='viridis', marker='x')
ax.set_title("Monthly stream Flow")




#%%
## Plot 3: Histogram 
mybins = np.linspace(0, np.log10(np.max(data["flow"])), num=15)
plt.hist(np.log10(data["flow"]), bins=mybins)
plt.title('Streamflow')
plt.ylabel('Count')




#%%
## Plot 4: Filled plot
monthly_max = data.groupby(data.month).max()
monthly_min = data.groupby(data.month).min()
monthly_mean = data.groupby(data.month).mean()

ax = plt.axes()
ax.plot(monthly_mean.flow)
ax.fill_between(monthly_mean.flow.index,
                    monthly_min.flow.values,monthly_max.flow.values, alpha=0.2)
ax.set_yscale("log")
ax.set_xlabel("month")
plt.axvline(3, color='black', linestyle='--')




# %%
