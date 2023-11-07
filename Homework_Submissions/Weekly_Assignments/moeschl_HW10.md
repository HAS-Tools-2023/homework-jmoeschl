### Jessi Moeschl
### 11/6/2023
### Homework 10

### Grade
3/3 - Nice work.  You are not alone in your confusion on functions and for loops many others feel the same and we will keep practicing!

I have added some answers to your questions below. 

## What I Learned:
I understood generally how matplotlib was used to creat graphs on tuesdays assignment.  I also understood how to read in a file with inclusion of the datetime part.  I felt way mroe comfortable with thursday's exercises though and those I was able to do mostly on my own from scratch (not building off answers in class).  I am completely lost on how to work functions though as well as the for loops in vs. out the function.


## What I Am Confused On:
1) 
From Tuesday's assignment, I am confused on what 

"iris_type='versicolor'
ax.scatter(iris_df.loc[iris_type]['sepal length (cm)']"

is doing.  I get that it is pulling the type in row one.  In row two thoug, why can't "iris_type" stand alone if it was defined in the row above?  Why is .loc[] still needed?
**Iris_type is just a varaible that we are setting equal to whatever type of iris we want to plot.  In the second line of code yo provided '.loc[iris_type]' is finding all of the rows that are of type iris_type we could have done the same thing without a variable by saying df.loc['versicolor']**

1) 
I do not get the difference between setting index vs. parse dates.  I also do not get the reading in a csv vs. a table besides that there is no "sep=" part.
**setting index is determining which column will be used as the row names. Parsing dates can be applied to any column and is telling python that the column is composed of dates not just strings so it knows how to handle them** 

3)
The code is broken in 2.4 for the average but works for the min and max.  i also do not know how to set x and y axis within the single line or the title.  I could get it separately added though.  Just the average was a lost cause wehn operating the same way as min and max.

**We'll go over this solution in class tomorrow**

4)
I also had a further question about one answer we went thorugh in class.  For each plot, do you need to start with "fig, ax = plt.subplots()"?
**In general yes if you are using the ax approach**