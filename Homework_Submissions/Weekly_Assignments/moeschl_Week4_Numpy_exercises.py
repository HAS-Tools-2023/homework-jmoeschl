#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np


# %% Exercise 1: Working with a 1-D array:
x = np.arange(0, 3**3)

# 1.1 What is the length of x?
len(x)                  # or use x.size as an attribute of numpy array
        # length = 27

# Comprehension question is this an attribute or a method or a function of x? How do we know?
        # FUNCTION but attribute is x.size

#%%
# 1.2 Get the first value out of x and print it: 

print(x[0])                     # or use 'x[x.size-1]       
                # prints '0'

#%%
# 1.3. Get the last value out of x and print it?

print(x[-1])      
                 # prints '26'

#%%
# 1.4. Get the first 5 values and last 5 values out of x and print them?

x[:5]           # colon means all the stuff up to 5 NOT INCLUSIVE
            # prints 'array([0, 1, 2, 3, 4])

x[-5:]          # or 'x[22:]'
            # prints 'array([22, 23, 24, 25, 26])

#to find length of array for above if not known:   new variable
        # array_length = len(x)
        # print(x[(array_length - 5):1])


#%%
# %% Exercise 2: Working with a 2-D array:
# 2.1 Get the first 9 values of x, and reshape them to a
#    3x3 matrix. Assign this matrix to the variable `y`
x_new = x[:9]
y = np.reshape(x_new, (3,3))
print(y)                                #prints [[0 1 2]
                                        #        [3 4 5]
                                        #        [6 7 8]]


#BONUS show how you can do this with two lines of code and how you can do it with one line of code. 

##Comprehension question: Is reshape a function, a method or an attribute of y?  How do we know? 

                # reshape is a function because it has np. before it
                        # if i did x.reshape then it is a method

#%%
# 2.2 Get the middle value out of y and print it?
y = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
])

y[1,1]                  #printed "4"


#%%
# 2.3. Get the first row out of y and print it?

y[0]                    #printed "array([0, 1, 2])"



# %%
# 2.4 If you save the first row of y to a new variable w what type of object is w? 

w = y[0]
print(w)
w.dtype

                        #printed [0 1 2]
                        #object type is int

#%%
# 2.5 Get the first column out of y and print the lenght of this colum? (hint you will need to use the attribute 'size' to do this)
y_column1= y[:,0]                  #prints [0 3 6]
y_column1.size                          # prints '3'


# BONUS: Try doing this two different ways. First where you save the column as a new variable and then get its size (i.e. with two lines of code). And next where you combine thos commands into one line of code

#%% Exercise 3 Creating numpy arrays: 

# %%
# 3.1 use the np.arange function and the reshape method to create a numpy array with 3 rows and two columns that has values 0-9
x = np.arange(6)
x = [0, 1, 2, 3, 4, 5]
np.reshape(x, (3,2))

# %%
# 3.2 use the np.ones function to create a 4 by 4 matrix with all ones 

x = np.ones((4,4))
print(x)

# %% 
# 3.3 Now modify the matrix you created in the last exercise to make the values all 4's   (Hint: you could do this with either addition or multiplication)

x * 4


#%% Exercise 4:  using the axis argument
z=np.arange(20).reshape((5,4))

# 4.1 Use 'sum' to print the total of z
np.sum(z)
                        #prints 190

#Comprehension question -- is 'sum' a function a method or an attribute?  
        #np.sum is a function
#%%
# 4.2. Print the sum along the first dimension of z?
first_dim = np.sum(z, axis= 0)
print(first_dim)
                        # prints [40 45 50 55]
## Comprehension question -- is the 'first dimension' the rows or the columns of z? 
 #first dimension is the rows

np.shape(first_dim)
np.shape(z)



# %% 
# 4.3 How many elements does your answer to exercise 4.2 have? (i.e. how many numberd did you get back?)

        #I got 4 numbers back

# How does this compare to the shape of z? 

        #the shape of the new arrray is [4,]
        #the shape of z is (5,4) which makes sense.  the first row has 4 columns
        
        