# %%
# Exercise 1: Given two arrays a and b, create a new array that contains the maximum value at each index
import numpy as np
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

c=np.zeros(len(a))

for i in range(7):
    print(i)
    c[i]=max(a[i],b[i])


# %% 
# Exercise 2: 
# Use a while loop to print out the cumulative sum of the array c
# (i.e. the first nubmer, then the sum of the first 2 numbers, then the first 3 numbers etc.) 

print(c)
i = 0
total = 0

while i < len(c):
    total += c[i]
    i += 1
    print(i, total)
