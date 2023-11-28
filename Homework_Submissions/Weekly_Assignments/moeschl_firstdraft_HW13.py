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

#%%     setting the forecast date and converting it to a datetime
forecast_date = '2023-11-30'
date1 = pd.to_datetime(forecast_date)

# %%            GETTING MY FLOW DATA FROM USGS

def readfile(station_id, start_date, stop_date):
    """
    Parameters (Inputs):
    Takes in a station id number, start date, and end date
    Returns (outputs):
    Creates a pandas dataframe from the USGS site for the stream flow data
    """
    obs_day = nwis.get_record(sites=station_id, service='dv', start=start_date, end=stop_date, parameterCd='00060')
    return(obs_day)

# VERDE NEAR CAMP VERDE DATAFRAME
verde = readfile(station_id = '09506000', start_date = '2022-11-27', stop_date = '2023-11-26')

# VERDE NEAR CLARKDALE
clarkdale = readfile(station_id = '09504000', start_date = '2022-11-27', stop_date = '2023-11-26')
    # ugly deserty and sunny site

# VERDE NEAR PAULDEN (HEADWATERS)
paulden = readfile(station_id = '09503700', start_date = '2022-11-27', stop_date = '2023-11-26')
      # one of my two favorite sites on the verde

#%%             CHAT GPT ASSISTED FOR GREATING GRAPHS IN A FUNCTION
def plot_stream_flow(data, forecast_date):
    """
    Plot USGS stream flow data and forecast for a given date.
    Parameters:
    - data (pandas DataFrame): Stream flow data DataFrame.
    - forecast_date (str): Forecast date for future data in the format 'YYYY-MM-DD'.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['00060_Mean'], label='Mean Streamflow')
    plt.title('USGS Stream Flow Data and Forecast')
    plt.xlabel('Date')
    plt.ylabel('Stream Flow (cfs)')
    plt.legend()
    plt.show()

plot_stream_flow(paulden, forecast_date)        # plot for paulden
plot_stream_flow(clarkdale, forecast_date)      # plot for clarkdale
plot_stream_flow(verde, forecast_date)          # plot for verde

#%%             API INCLUSION
# I chose to use a location around the Paulden area that had a snow_accum variable.
# I chose this because although there is none right now, this could be useful in the future
# also I find it interesting around the Paulden area as it is the verde headwaters but spring fed so snow plays an interesting role
mytoken = 'd7cb3f51f3fa469c8464f3509c1e53ae'
base_url = "http://api.mesowest.net/v2/stations/timeseries"
args = {
    'start': '202211270000',
    'end': '202311261200',
    'obtimezone': 'UTC',
    'vars': 'snow_depth',
    'stids': 'COOPJRMA3',
    'units': 'temp|F,precip|cm',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
print(apiString)

fullUrl = base_url + '?' + apiString
print(fullUrl)                    # all above this is a url request
                                  # can be replaced with online created url

response = req.urlopen(fullUrl)     #loads it as a dictionary
responseDict = json.loads(response.read())

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']                      # my x axis
snow_accum = responseDict['STATION'][0]['OBSERVATIONS']['snow_depth_set_1']             # my y axis

# my graph of the snow so far in november
f, ax = plt.subplots()              
ax.plot(dateTime, 
        snow_accum, 
        color="blue",
        label='snow')
ax.set(title="Accumulated Snow")
plt.tick_params('x', rotation=80)
plt.legend(loc='upper right')
plt.show()


#%%     ONE OF MY FUNCTION

def monthly_mean(dataframe, year, month):
    """
    calculates per given month the average stream flow for the year
    Parameters (Inputs):
    takes in the given dataframe (gage) and a month and year from the given forecast date above
    Returns (outputs):
    the average for that month at that site of stream flow
    """
    date = '{0}-{1}'.format(year,month)             # asked chatgpt how to do this
    meanval=np.mean(dataframe['00060_Mean'][date])
    return(meanval)
  
monthly_mean(paulden, date1.year, date1.month)


paulden_new = monthly_mean(paulden, date1.year, date1.month)
clarkdale_new = monthly_mean(clarkdale, date1.year, date1.month)
verde_new = monthly_mean(verde, date1.year, date1.month)


#%%     FORECAST

oneweek = verde_new + clarkdale_new - paulden_new
twoweek = clarkdale_new + verde_new 

print("1 week forecast = ", oneweek)
print("2 week forecast = ", twoweek)

