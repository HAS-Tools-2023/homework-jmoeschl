# Tuesday
import pandas as pd
import numpy as np
import urllib
import matplotlib.pyplot as plt


#%%
### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean of every colum of the dataframe
# If you have time try doing it with and without a for loop (You can either use the function inside your for loop or put a for loop inside your function)

def average_columns(my_array):
    ncol=my_array.shape[1]
    col_mean=np.zeros(5)
    for i in range(ncol):
        col_mean[i]= np.mean(my_array[:,i])
    return(col_mean)

average_columns(data)


#%% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset. 
# This dataset comes with the sklearn pacakge so we can just load it in directly. 
# It describes measurements of sepal & petal width/length for three different species of iris
iris_df = pd.read_csv('iris_df.csv', index_col='species')


# %%
# 1. How do you view the "unique" species in the `iris_df` index?
#hint use the function np.unique() and apply it to the index of the dataframe

unique_species = np.unique(iris_df.index)

# %%
# 2. How do you "locate" only rows for the `versicolor` species?
#Hint use .loc to the rows that have the name 'versicolor'

iris_df.loc['versicolor']

# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 
# look back at our pandas examples Use groupby.mean

mean_column = iris_df.groupby('species').mean()

## OR

species_mean = iris_df.groupby(iris_df.index).mean()

# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` for the `versicolor`` species?
#hit first grab out just the rows you want to plot 
#Then use scatter plot function to plot the columns you want (plotting notes)

ax = plt.figure(figsize=(10,10))

versicolor_df = pd.DataFrame(iris_df.loc['versicolor'])
ax = versicolor_df.plot.scatter(x='', y='', s=50)


LAURAS VERSION:

ax = plt.axes()
ax.scatter(iris_df.loc['versicolor']['sepal length (cm)'], iris_df.loc['versicolor']['petal length (cm)'], marker='o')
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('petal length (cm)')
ax.set_title('Versicolor')

# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. (BONUS: Try to write the code so you only need to type each iris name one time)

#Repeat what you did in 4 three times

LAURAS VERSION:

ax = plt.axes()
iris_type='versicolor'
ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'],
           iris_df.loc[iris_type]['petal length (cm)'], marker = 'o', color = 'tomato', label='versicolor')
iris_type='setosa'
ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'],
           iris_df.loc[iris_type]['petal length (cm)'], color = 'darkcyan', marker = 'o', label = iris_type)
iris_type='virginica'
ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'],
           iris_df.loc[iris_type]['petal length (cm)'], marker = 'o', color = ' darkviolet', label=iris_type)
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('petal lenth (cm)')
ax.set_title(iris_type)
ax.legend()

# 6. Write a function that will do 'ax.scatter' for a given iris type and desired color of points and use this to function to modify the code you make in 5

#HINT no for loop needed, the function should have two arguments and you will call it 3 times. 
#Copy your code from #5 down here and replace your ax.scatter calls with your function. 

DAVES:

versicolor_df = iris_df[iris_df.index == 'versicolor']
setosa_df = iris_df[iris_df.index == 'setosa']
virginica_df = iris_df[iris_df.index == 'virginica']

#input is species dataframe and color
def plot_iris(species_data, color):
    fig, ax = plt.subplots()
    ax.scatter(species_data['petal length (cm)'], species_data['sepal length (cm)'],
               marker = 'x', color='black', title='petal length and sepal length')



DR CONDONS VERSION:

def iris_scatter(iris_type, plot_color):
    ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'],
               iris_df.loc[iris_type]['petal length (cm)'],
               maker = 'o', color = plot_color, label=iris_type)
    
ax = plt.axes()
iris_scatter(iris_type='versicolor', plot_color='tomato')
iris_scatter('setosa', 'darkcyan')
iris_scatter('virginica', 'darkviolet')
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('petal length (cm)')
ax.set_title(iris_type)
ax.legend()
# %%





#%% Thursday
#Thursday

# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 

#MINE:

data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=31, 
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                            index_col=['datetime'],
                            parse_dates=['datetime'])

#%% 2.1

# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 

#MINE
columns=['date', 'year', 'yday', 'dayL (s)', 'prcp (mm/day)','srad (W/m^2)', 
       'swe (kg/m^2)', 'tmax (deg c)',	
       'tmin (deg c)','vp (Pa)']
datatwo = pd.read_csv('daymet.csv', names=columns, 
                     parse_dates=['date'], index_col=['date'])

#%% 2.2

#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 
#MINE
print(datatwo.describe())
datatwo.info()

#%% 2.3

#2.3  Make a scatter plot of day length (dayl) vs maximum temperature. Fit a trend line 

#ax = plt.axes()

fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.scatter(datatwo['dayL (s)'], datatwo['tmax (deg c)'],
                color='blue')

#%%

#2.4 Make a plot with three lines (1) average, (2) min and (3) max shortwave radiation (srad) vs the day of the year (i.e. 1-365)
# MY CALCS
doymax=datatwo.groupby('yday').max()
doymin=datatwo.groupby('yday').min()
#doyavg=datatwo.groupby('yday').mean()      #broken???

plt.plot(doymax.index, doymax['srad (W/m^2)'], color='red')
plt.plot(doymin.index, doymin['srad (W/m^2)'], color='yellow')
#plt.plot(doyavg.index, doymin['srad (W/m^2)'], color='purple')
