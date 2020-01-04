"""Write a program that generates 100 random integers that are either 0 or 1. 
Then ﬁnd the longest run of zeros, the largest number of zeros in a row. 
For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4."""

from random import randint
t = []
for i in range(100):
    t = t + [randint(0,1)]
    #t.append(randint(0,1))
print(t)

maxC = 0
c_0 = 0
for i in range(100):
    if t[i] == 0:
        c_0 = c_0 + 1
    if t[i] == 1:
        if maxC < c_0:
            maxC = c_0
        c_0 = 0
print(maxC)