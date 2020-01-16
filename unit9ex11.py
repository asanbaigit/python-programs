"""
Write a program that starts with an 5×5 list of zeroes and randomly changes exactly ten of 
those zeroes to ones"""
from random import sample
L = [[0]*5]*5
print(L)
c = 0

while c < 5 :
    c = c + 1
    L = L.replace((sample(L,2)),'1')

print(L)


