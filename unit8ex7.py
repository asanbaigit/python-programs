"""  Write a program that estimates the average number of drawings it takes before the user’s numbers are picked in a
 lottery that consists of correctly picking six different numbers that are between 1 and 10. To do this, run a loop
  1000 times that randomly generates a set of user numbers and simulates drawings until the user’s numbers are drawn. 
  Find the average number of drawings needed over the 1000 times the loop runs. """

from random import sample
c= 0
l = [i for i in range (1,11)]
t = sample(l,3)
print(t)
print()

for h in range(1,1001):
    k = [j for j in range (1,11)]
    s = sample(k,3)
    if s == t:
        print(s)
        c = c+1
    
print(c)