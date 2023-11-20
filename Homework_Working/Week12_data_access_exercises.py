# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis

# %%
# Exercise 1: 
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 


#%%     using option 1

def readfile(site, start, stop):
    url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + stop
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],parse_dates=['datetime'], index_col=['datetime'])
    return(data)

twenty = readfile(site = '09506000', start = '2019-01-01', stop = '2020-12-31')
print(twenty)
    

#%%     Using option 3

def readfile(station_id, start_date, stop_date):
    obs_day = nwis.get_record(sites=station_id, service='dv', start=start_date, end=stop_date, parameterCd='00060')
    return(obs_day)

march = readfile(station_id = '09506000', start_date = '2023-03-01', stop_date = '2023-04-01')

print(march)



# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 


#3. Make a timeseries plot showing the data from all 3 gauges. 


# %%
# Exercise 2: 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json 
import urllib.request as req
import urllib

#%%
#1. Download the dataset from the class notes and determine what (1) type of python object the station observations are and (2) what all variables are included in the observations. 

mytoken = 'd7cb3f51f3fa469c8464f3509c1e53ae'

# This is the base url that will be the start our final url
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data that we want
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': mytoken} 

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Now we are ready to request the data
# this just gives us the API response... not very useful yet
response = req.urlopen(fullUrl)

# What we need to do now is read this data
# The complete format of this 
responseDict = json.loads(response.read())

# Long story short we can get to the data we want like this: 
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_daily = data.resample('D').mean()



#%%
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
#  responseDict['STATION'][0]['OBSERVATIONS'].keys()
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip_accum = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

# %%  if used the online url instead




