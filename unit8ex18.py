"""Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the following:
(a) Print the list. (b) Find the largest value in the third row. (c) Find the smallest value in the sixth column."""
from random import randint
"""
L =[]
for i in range(10):
    t = []
    for j in range(10):
        t.append(randint(1,100))
    L.append(t)
print(L)
"""
# a
L = [[randint(1,100) for i in range (10)] for j in range (10)]
for l in L:   # for i in range (len(L))
    print(l)   # print(L[i])
#b
print(max(L[2]))
#c
print(min(L[5]))