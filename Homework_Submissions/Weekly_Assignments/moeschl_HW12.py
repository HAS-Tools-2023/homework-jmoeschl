#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json 
import urllib.request as req
import urllib
import os
import dataretrieval.nwis as nwis

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

#%%             API INCLUSION
mytoken = 'd7cb3f51f3fa469c8464f3509c1e53ae'
base_url = "http://api.mesowest.net/v2/stations/timeseries"
args = {
    'start': '202311120000',
    'end': '202311200200',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|cm',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
print(apiString)

fullUrl = base_url + '?' + apiString
print(fullUrl)                    # all above this is a url request
                                  # can be replaced with online created url

response = req.urlopen(fullUrl)     #loads it as a dictionary
responseDict = json.loads(response.read())

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip_accum = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

print(precip_accum[0])

#               plotting the api
f, ax = plt.subplots()              
ax.plot(dateTime, 
        precip_accum, 
        color="blue",
        label='flow')
ax.set(title="Accumulated Precipitation")
plt.tick_params('x', rotation=45)
plt.legend(loc='upper right')
plt.show()

#%%     NOVEMBER DATA FRAME AND GRAPH

november = data_frame[data["month"] == 11]
november_data = november.mean()

#print(november_data)

f, ax = plt.subplots()
ax.bar(x=november.day, 
        height=november.flow, 
        color="orange",
        label='max flow')
ax.set(title="Max Flow on Each Day of November")
plt.legend(loc='upper right')
plt.show()
 
#%%     CALCULATING

november_flow = november[["flow"]]

#     ONE WEEK FORECAST VARIABLE
onewkcalc = (november_flow.mean())/(november_flow.std())        # making a ratio
oneweek = onewkcalc * november_flow.std()                       # deciding a higher value
oneweekrain = oneweek + precip_accum[-1] - precip_accum[0]      # adding precip although in different units (note that did the difference)

#     TWO WEEK FORECAST VARIABLE
twowkcalc = (november_flow.mean())/(november_flow.std())
twoweek = twowkcalc * november_flow.mean()                      # the lower of the two possibilities
twoweekrain = twoweek + precip_accum[-1] 

#%%     PRINT STATEMENTS
print("1 week forecast = ", oneweekrain[0])
print("2 week forecast = ", twoweekrain[0])



# %%            TUESDAY CLASS EXERCISES

# Exercise 1: 
# 1. Write a function that takes the following arguments as inputs: 
def readfile(site, start, stop):
    url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + stop
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],parse_dates=['datetime'], index_col=['datetime'])
    return(data)

twenty = readfile(site = '09506000', start = '2019-01-01', stop = '2020-12-31')
print(twenty)
    
#     Using option 3
def readfile(station_id, start_date, stop_date):
    obs_day = nwis.get_record(sites=station_id, service='dv', start=start_date, end=stop_date, parameterCd='00060')
    return(obs_day)

march = readfile(station_id = '09506000', start_date = '2023-03-01', stop_date = '2023-04-01')
print(march)            # coolest flow period

# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 

childs = readfile(station_id = '09508000', start_date = '2023-03-01', stop_date = '2023-04-01')
print(childs)     # ugly deserty and sunny site

paulden = readfile(station_id = '09503700', start_date = '2023-03-01', stop_date = '2023-04-01')
paulden_df = pd.DataFrame(paulden, columns=['00060_Mean', '00060_Mean_cd', 'site_no'])
print(paulden_df)          # one of my two favorite sites on the verde

#3. Make a timeseries plot showing the data from all 3 gauges. 

f, ax = plt.subplots()              
ax.plot(paulden.index, 
        paulden_df['00060_Mean'], 
        color="orange",
        label='flow')
ax.set(title="Flow on Each Day of March - Paulden")
plt.tick_params('x', rotation=45)
plt.legend(loc='upper right')
plt.show()

f, ax = plt.subplots()              
ax.plot(childs.index, 
        childs['00060_Mean'], 
        color="blue",
        label='flow')
ax.set(title="Flow on Each Day of March - Childs")
plt.tick_params('x', rotation=45)
plt.legend(loc='upper right')
plt.show()


#%%                THURSDAY CLASS EXERCISES

#1. Download the dataset from the class notes and determine what (1) type of python object the station observations are and (2) what all variables are included in the observations. 

mytoken = 'd7cb3f51f3fa469c8464f3509c1e53ae'
base_url = "http://api.mesowest.net/v2/stations/timeseries"

args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
print(apiString)

fullUrl = base_url + '?' + apiString
print(fullUrl)

response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))
data_daily = data.resample('D').mean()

#2. Modify the API call to return accumulated precipitation instead (variable name = 'precip_accum', set the units to 'metric') and make a plot of the daily max accumulated precipitation
mytoken = 'd7cb3f51f3fa469c8464f3509c1e53ae'
base_url = "http://api.mesowest.net/v2/stations/timeseries"
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'metric',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
print(apiString)

fullUrl = base_url + '?' + apiString
print(fullUrl)                    # all above this is a url request
                                  # can be replaced with online created url
response = req.urlopen(fullUrl)     #loads it as a dictionary
responseDict = json.loads(response.read())

#  to what to change the bottom variable to precip instead of temp
responseDict['STATION'][0]['OBSERVATIONS'].keys()
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip_accum = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']







