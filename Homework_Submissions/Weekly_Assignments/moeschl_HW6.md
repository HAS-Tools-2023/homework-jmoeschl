### Jessi Moeschl
### 10/8/2023
### Homework 6

###
2/3: Good work I subtracted one since you were missing 5 and didn't get 4 right. 
- Note for number 4 I was looking for the hightes and lowest values not the first and last so you needed to do a sort before doing the head/tail operation. 
- No worries on the plotting we are going to work on plotting this week :) 
- I have posted a solution for this weeks homework please check it out and come by my office hours if anything is still unclear. 

### Forcast Selection

I chose this weeks values to be in the 70's (78 and 72) as flow has been abnormally low and I am not confident that after the next day or two there will be more rain. 


### Summary of Method

1. making my data frame
2. see if it worked (.describe)
3. get rid of bad data (.dropna())
4. checked if flow was its own column
5. did a general stats run (max, min, mean)
6. create a separate variable of only october flows
7. october statistics (max, min, mean)



### Problems

I could not get a plot to work.  I used "data_frame.plot.bar(['day', 'flow'])" to try and plot the day versus flow.  I need general assistance here.

I also struggled to use the "&" to get flows for a specific day of all years.


### Assignment Questions

1. Column Names: Flow, Year, Month, Day
    The index is each data point and the types are integers
2. Flow min: 19
    Flow max: 42,200
    Flow mean: 319
    Quartiles: 87, 147, 207
    Stdev: 1,161
3. October:
    Min: 59.8
    Max: 1910
    Mean: 144.8
    Quartiles: 101, 119, 146
    Stdev: 131.8
    
4. data_frame.head(5):

    flow  year  month  day
0  208.0  2000      1    1
1  213.0  2000      1    2
2  214.0  2000      1    3
3  211.0  2000      1    4
4  212.0  2000      1    5

data_frame.tail(5):

     flow  year  month  day
8638  100.0  2023      8   26
8639   86.8  2023      8   27
8640   74.4  2023      8   28
8641   65.2  2023      8   29
8642   58.8  2023      8   30