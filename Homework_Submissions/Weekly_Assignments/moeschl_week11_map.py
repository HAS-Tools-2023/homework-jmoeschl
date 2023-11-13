#%%  Imports
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import os
import fiona
from shapely.geometry import Point
import contextily as ctx

#%% 1. Opening Shape Files (all files are from class)
# 1. Open the arizona_huc8_shapefil and the arizona_shapefile following the example we did in class. 

file =  os.path.join('data11_7/arizona_huc8_shapefile', 'WBDHU8.shp')
huc8 = gpd.read_file(file)

file = os.path.join('data11_7/arizona_shapefile', 'tl_2016_04_cousub.shp')
arizona = gpd.read_file(file)

file =  os.path.join('data11_7/gagesii_shapefile', 'gagesII_9322_sept30_2011.shp')
gages_file = gpd.read_file(file)

gages_file.STATE.unique()
gages = gages_file[gages_file['STATE']=='AZ']       # creating a dataframe of only arizona gages

#%% 2. Exploring Properties
# 2. Explore their properties and attributes and be able to explain (1) what type of geometry each is, (2) how many features there are, (3) what attributes each feature has. 

huc8.describe()
arizona.decribe()
huc8.head()
arizona.head()
huc8.columns
arizona.columns
huc8.geom_type              #polygons
arizona.geom_type

#%% 3. Plotting the basic maps
# 3. Plot each dataset. You can plot them separately but also try plotting subsets and plotting them on top of each other. 

fig, ax = plt.subplots(figsize=(10, 10))
huc8.plot(ax=ax)                            # plotting the watershed boundaries of huc8
plt.show()

fig, ax = plt.subplots(figsize=(10, 10))
arizona.plot(ax=ax, color = 'brown')        # plotting just arizona
plt.show()

fig, ax = plt.subplots(figsize=(10, 10))
gages.plot(ax=ax, color = 'green', marker = 'o')        # plotting just the az gages
plt.show()

#%% Begin Excercise 2.... Geodatabase
# 1. Open the WBD_15_HU2_GDB geodatabase and select a different layer to plot than the one I showed (i.e. not HUC6)
file =  os.path.join('data11_7/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
fiona.listlayers(file)
HUC10 = gpd.read_file(file, layer="WBDHU10")

# read in the geodatabase and pulled the hcu10 layer out

HUC10.head()        # just checking what the layer contains for info

#%% 2. Creating new random points
# 2. Create a geodatabase with the two points of interest I showed (i.e. UA and the stream gauge) as well as two additional points of your choosing

point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333],
                       [-112.0740373, 33.4483771],      # flagstaff (i think)
                       [-111.325134, 34.230869]])       # payson

point_geom = [Point(xy) for xy in point_list]

#mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC10.crs)      # put in huc 10 projection


#%% 3. Some individual maps (before projections)
#3. Make a map of your selected datasets. If you have time experiment with changing the markers and lines/fill colors on your plot 

# the huc10 plot witht he points overlayed
fig, ax = plt.subplots(figsize=(10, 10))
HUC10.plot(ax=ax, color = 'deepskyblue')
point_df.plot(ax=ax, color='red', marker='*')
ax.set_title("HUC Boundaries")
ax.set_ylabel("Longitude")
ax.set_xlabel("Latitude")
plt.show()

# the arizona map with the points overlayed
fig, ax = plt.subplots(figsize=(10, 10))
arizona.plot(ax=ax, color = 'burlywood')
point_df.plot(ax=ax, color='red', marker='*')
ax.set_title("Arizona")
ax.set_ylabel("Longitude")
ax.set_xlabel("Latitude")
plt.show()

#%%     PROJECTION CHANGES

points_project = point_df.to_crs(arizona.crs)
HUC10_project = HUC10.to_crs(arizona.crs)
gages_project = arizona.to_crs(arizona.crs)


#%% TOTAL MAP (with projections to arizona)
# correct latitude and longitudes but the colors are not doing what they should
# i think that gages and arizona flip flopped, not sure how
# the next graph is the pretty one
fig, ax = plt.subplots(figsize=(10, 10))
HUC10_project.plot(ax=ax, color = 'deepskyblue')
arizona.plot(ax=ax, color = 'darkgoldenrod', alpha=0.7)
gages_project.plot(ax=ax, color = 'black', marker = 'o', markersize=10)
points_project.plot(ax=ax, color='red', marker='*')
ax.set_title("HUC Boundaries")
ax.set_ylabel("Longitude")
ax.set_xlabel("Latitude")
ctx.add_basemap(ax, crs=arizona.crs)
plt.show()


# %%   If I made the gages the base projection:
# this looks better, just the latitude and longitudes are wrong
points_project = point_df.to_crs(gages.crs)
HUC10_project = HUC10.to_crs(gages.crs)
arizona_project = arizona.to_crs(gages.crs)

fig, ax = plt.subplots(figsize=(10, 10))
HUC10_project.plot(ax=ax, color = 'deepskyblue')
arizona_project.plot(ax=ax, color = 'darkgoldenrod', alpha=0.7, label='arizona')
ax.legend(loc='upper right')
gages.plot(ax=ax, color = 'lightgrey', marker = 'o', markersize=10, label='gages')
ax.legend(loc='upper right')
points_project.plot(ax=ax, color='red', marker='*', label='self defined points')
ax.legend(loc='upper right')
ax.set_title("HUC Boundaries")
ax.set_ylabel("Longitude")
ax.set_xlabel("Latitude")
ctx.add_basemap(ax, crs=gages.crs)
plt.show()

# %%
