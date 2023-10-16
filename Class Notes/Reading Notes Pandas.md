#%%
import pandas as pd
import numpy as np 
import matplotlib as plt
#%%     PANDAS BASIC

can work with cells across a row, column, or a cells byt location or value

use the function "pd.DataFrame" to manually define a DataFrame
- could do this by providing column names and data values

- example:
dataframe = pd.DataFrame(columns=["column1", "column2"],
                         data=[
                             [value_column1, value_colum2],
                             [value_column1, value_column2]
                         ])


- numerical example:
avg_monthly_precip = pd.DataFrame(columns=["month", "precip_in"],
                                    data=[
                                      ["Jan", 0.70], ["Feb", 0.75], ["Mar", 1.85], ["Apr", 2.93]
                                    ])


#%%  

- PLOTTING
could use matplotlib or .plot()

- example (using .plot()):
f, ax = plt.subplots()
avg_monthly_precip.plot(x="month",
                        y="precip_in",
                        title="Plot of Pandas"
                        ax=ax)
plt.show()


- example(using matplotlib)
f, ax = plt.subplots()
ax(avg_monthly_precip.month,
    avg_monthly_precip.precip_in)
ax.set(title="Plot")
plt.show()

#%%     

- IMPORT CSV INTO DATAFRAME
must import os first!

- example:
fname=os.path.join("earthpy-downloads", "avg-precip-months-season.csv")
avg_monthly_precip = pd.read_csv(fname)

#%%

- RUN CALCULATIONS AND SUMMARIZE DATA
call a method by ".method_name()" AFTER the name of the object
object_name.method()

- attributes and functions
1) .head() and .tail()      for first and last rows (automatic 5)
ex: dataframe.head()

2) .info()                  for all info about dataframe
ex: avg_monthly_precip.info()
gives a lot of info

3) .columns                 to see the column names
ex: avg_monthly_precip.columns
output is index([mnths, precip, season])

4) .shape                   to see number of rows and columns
ex: avg_monthly_precip.shape
output is (12,3)

- summary stats
".describe()" to get summary of all data
        -outputs the count, mean, minimum, and maximum
        -can also do on individual columns w/ DOUBLE brackets (for a dataframe)
        ex: avg_monthly_precip[["precip"]].describe() 
        -could do single bracket but makes column 1d array
".median()"
".sum()"

- sort values:
in numpy could get a max and min but not when it occured
".sort_values()"
input is name of column to sort and a Boolean value for ascending 
     ex: dataframe.sort_values(by="column_name", ascending = True)

- ex:
avg_monthly_precip.sort_values(by="precip", ascending=False)
makes descending order (highest value at top)

- regular math calcs
dataframe["column_name"] *= 25.4
    -this multiplies everything by 25.4 in the column
to convert precip column from inches to millimeters:
    avg_monthly_precip["precip"] *= 25.4

- create new column w/ math calcs
dataframe['column_name_2"] = dataframe["column_name_1"] / 25.4
    - if column 2 already exists (the name) it will replace the values
    - otherwise it will create a new column AT THE END of dataframe

- ex:
avg_monthly_precip["precip_in"] = avg_monthyl_precip["precip"] / 25.4

- PLOT THE DATA EX. (histogram/bar plot)
f, ax = plt.subplots()
ax.bar(x=avg_monthly_precip.months, 
        height=avg_monthly_precip.precip, 
        color="purple")
ax.set(title="Plot of Average Monthyl Precipitation in mm")
plt.show()

- group common values
dataframe.groupby(['label_column'])[["value_column"]].method()
label_column: creates groups 
value column: column summarized for each group

# DO THIS FOR THE MONTHS (GROUPBY THE MONTHS)

flow_by_month=dataframe_thing.groupby(["month"])[["flow"]].describe()

- ex of grouping
precip_by_season=avg_monthly_precip.groupby(["seasons"])[["precip"]].describe()

- PLOT GROUP DATA
when type "precip_by_season.columns"
output: "multiindex([('precip', 'count'),
                    'precip', 'mean']),
                    etc.
drop a level then so only one index:
    precip_by_seasons.columns = precip_by_seasons.columns.droplevel(0)
then to plot the bars:
    f, ax = plt.subplots()
    ax.bar(precip_by_season.index,
            precip_by_season["mean"],
            color="purple")
    ax.set(title="Bar Plot of Seasonal Monthly Precip in mm")
    plt.show()

- for assignment:
flow_by_months.columns = flow_by_months.columns.droplevel(0)
f, ax = plt.subplots()
    ax.bar(flow_by_months.index,
            flow_by_months["mean"],
            color="purple")
    ax.set(title="Bar Plot of Seasonal Monthly Precip in mm")
    plt.show()

- other stats in groupby
.count() for number of rows ina  group
.median()
.sum()
.mean()

- ex. that creates new dataframe from stats
avg_monthly_precip_median = avg_monthly_precip.groupby(["seasons"])[["precip"]].median()
index becomes seasons and that is no longer a column
to avoid the new index:
    avg_monthyl_precip = avg_monthly_precip.groupby(["seasons"], as_index=False)[["precip"]].median()


#%% SELECT DATA FROM PANDAS DATAFRAME

- indexing
location based: ".iloc" to provide row and column but as a range (first inclusive and second not)
ex: dataframe.iloc[0:1, 0:1]    ## to get first row and first column
label based: ".loc" with a column name
ex: dataframe[dataframe["column"] == value]     ## returns all rows of value in that column

- for assignment try:
dataframe[dataframe["month"] == "october"]

- example to get first row and first two column 
avg_monthly_precip.iloc[0:1, 0:2]
returns "0  jan  0.7"

- another iloc example
to select an entire row or column
dataframe.iloc[0:1, :]  OR  dataframe.iloc[:, 0:1]
ex: avg_monthly_precip.iloc[0:1, :]
    output: "0  jan 0.7 winter"

- using .loc
avg_monthly_precip_index = avg_monthly_precip.set_index("months")
makes "months" the index instead of a column
    -not in the index, it is the index
now can use ".loc" to find dats from dataframe using the value in the months index
ex:
    avg_monthly_precip_index.loc[["Aug"]]

- for assignment
dataframe_index = dataframe.set_index("month")
dataframe_index.loc[["Oct]]

- selct data using columns
dataframe["column"]
ex:
    avg_monthly_precip["months"]
    OR
    avg_monthly_precip[["months"]]  to output in pretty (Pandas dataframe)
can do several columns:
    avg_monthly_precip_text  avg_monthly_precip[['months', 'seasons']]




## USE BELOW IN HW

- filter data using specific values
avg_monthly_precip[avg_monthly_precip["seasons"] == "Summer"]
gives all rows (the entire row) tht the season is summer

- so for assignment:
October_Data = dataframe[dataframe["month"]  == 10]

- for assignment, check what is below a flow value
dataframe[dataframe["flow"] <= 60]



