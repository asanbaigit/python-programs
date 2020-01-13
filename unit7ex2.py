"""Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list. (b) Print the average of the elements in the list. 
(c) Print the largest and smallest values in the list. 
(d) Print the second largest and second smallest entries in the list 
(e) Print how many even numbers are in the list."""
#a
from random import randint
l = []
mini = 101
mini2 = 101
maks = 0
maks2 = 0
even = 0
for i in range (20):
    x = randint (1,100)
    if x > maks:
        maks2 = maks
        maks = x
    elif x > maks2 and maks > maks2:
        maks2 = x
        
    if x < mini:
        mini2 = mini
        mini = x
    elif x < mini2 and mini < mini2:
        mini2 = x

    if x % 2 == 0:
        even = even + 1
    l.append(x)

print('This is the list ',l)
#c
b=0
for i in range (len(l)):
    b = b+l[i]
print(b/(len(l)),' is the average of the elements in the list')
#c
print (mini,' is the smallest value in the list','and the ',maks,' is the largest value in the list ')
#e
print('The are ',even,' even numbers in the list')

#d
print (maks2,' is the second largest number in the list')
print (mini2,' is the second smallest number in the list')

# print (min(l)) prints minimum in l
# print (max(l)) prints maximum in l
# print (sum(l)/len(l)) prints average of l


