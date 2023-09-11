# %%
# This set of exercises works through
# some basic python functionality
# I'll still be using some functions from 
# numpy but nothing you write should need it
# although you can use it if you'd like
import numpy as np

# %%  1.)
# Write code to translate a boolean value
# to a string using a conditional statment.
#  Specifically, if the `testval` 
# is `True` then print "Yes" and if it is
# `False` then print "No"

import numpy as np

testval = bool(np.random.choice([0, 1]))
# TODO: Your code here

print(testval)

if testval == True:  
    print ('Yes')
else:
    print ('No')

message = None
# ...
print(message)

#1.b Can you translate this to a string without a conditional statement?

# %% 2.)
#Given the following list write print statements that spell the word 
#'bad' as many ways as possible by pulling from mylist
mylist = ['a', 'b', 'c', 'd']

# %% 3.)
# You will be given a random integer, and 
# your goal is to return the same value, but
# as a negative number. Notice, the number you
# are given may already be negative
testval = np.random.random_integers(-100, 100)
# TODO: Your code here
negval = None
print(testval, negval)


# %% 3.)
# Time for a coding interview classic, FizzBuzz
# The rulse of the game:
#  - print numbers from 1 to 100
#  - if the number is divisible by 3 print "Fizz"
#  - if the number is divisible by 5 print "Buzz"
#  - if the number is divisible by both 3 and 5 print "FizzBuzz"
#  - otherwise, print the number
testvals = np.arange(1, 101)
#TODO: Your code here
# ...
for v in testvals:
    print('NONE')

# %%
