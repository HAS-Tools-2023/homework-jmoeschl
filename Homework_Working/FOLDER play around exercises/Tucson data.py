#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#%% ### Define column names and read csv file 
col_names = ['Station_ID','Date_Time','air_temp_set_1','dew_point_temperature_set_1','relative_humidity_set_1','wind_speed_set_1','wind_direction_set_1','dew_point_temperature_set_1d']

data = pd.read_csv('Tucson data.csv', skiprows=8, parse_dates=[1], names=col_names)


### Set index to be date column
data = data.set_index(data['Date_Time'])

print(data)


#%% ### Assign variables to data columns 

date = data.index
temp = data['air_temp_set_1']
td = data['dew_point_temperature_set_1d']
rh = data['relative_humidity_set_1']
wind_spd = data['wind_speed_set_1']
wind_dir = data['wind_direction_set_1']


#%%     PULL OUT A SINGLE WEEK
temp_1week = temp["2023-07-01":"2023-07-07"]


#%%     FUNCTION FOR SOME DATA TO BE CONVERTED C TO F

def c2f(data1):
    new_data = (9/5 * data1) + 32
    return new_data

# then to change air temp to that

temp_f = c2f(data1=temp)
td_f = c2f(data1=td)



#%%     BASIC FUNCTION FOR NAME
def hello(name, place):
    text = "Hello {0} you are from {1}".format(name,place)

    return text

# then to call it do :
hello(name="Jessi", place="Phoenix")
# %%    FUNCTION FOR ANY DATA TO BE FROM METRIC TO IMPERICAL UNITS

def metric_to_imperical(data1, wind=False):    #default behavior is that wind will be false unless set to true (need to include in call then)
    if wind == False:
        new_data = (9/5 * data1) + 32
    if wind == True:
        new_data = data1 * 1.94
    return new_data

temp_f = metric_to_imperical(data1=temp)
    # this would convert the temp
    # returns the new_data of "if wind == False"
wind_kt = metric_to_imperical(data1=wind_spd, wind=True)
    # this converts wind speed to true
    # returns the new_data of "if wind == True"



#%%     DEFINE A PLOTTING FUNCTION FOR SEVERAL METRICS

def plot_func(data1, data_title, color1):
    fig = plt.figure(figsize=(8,6))
    plt.title("KTUS July Data of {}".format(data_title))    #sqiggle because we dont know what we input yet: data title is like td and temp
    plt.xlabel("date")     
    plt.ylabel(data_title)
    plt.tick_params('x', rotation=45)
    plt.plot(data1.index, data1, color=color1)
    plt.show()

plot_func(temp_f, data_title="Temperature", color1='orange')
plot_func(td_f, data_title="Dew Point", color1='green')
plot_func(rh, data_title="Relative Humidity", color1='blue')

plot_func(temp_f['2023-07-01'], data_title="Temperature", color1='orange')
plot_func(temp_f['2023-07-01 00:00': '2023-07-01 12:00'], data_title="Temperature", color1='orange')


#%%     PLOT EVERYTHING ON SAME AXES (not a function)

fig = plt.figure(figsize=(8,6))
plt.title("KTUS July Weather Data")
plt.xlabel("Date")
plt.ylabel("Temperature degF")
plt.tick_params('x', rotation=45)
plt.plot(data.index, temp_f, color='orange', linewidth= 0.5, label="temp")
plt.plot(data.index, td_f, color='green', linewidth=0.5, label="dew point")
plt.legend()
plt.twinx()
plt.ylabel('RH %')
plt.plot(data.index, rh, color='blue', linewidth=0.5, label = "humidity")
plt.legend()
plt.show()






  



