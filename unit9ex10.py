"""
Write a program that has a list of ten words, some of which have repeated letters and some which don’t. 
Write a program that picks a random word from the list that does not have any repeated letters """
from random import sample
from random import choice
"""s= ''
l=[]
t='abcdefghijklmnopqrstuvwxyz'
for i in range (len(t)):
    s = s + t[i] + ' '
    l = s.split( )
L = l
L2=[]
for j in range(10):
    L2.append(sample(L,10))

print(L2)
print(s)"""
l=['azamat','alihan','adilia','altynbek','elnura']
while True:
    print(choice(l))
    break



