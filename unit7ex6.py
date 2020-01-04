"""Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49 
(b) A list containing the squares of the integers 1 through 50. 
(c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z."""

#a
a=[]
for i in range (50):
    a.append(i)
print(a)
#b
b=[]
for i in range (50):
    b.append(i*i)
print(b)
#c
t='abcdefghijklmnopqrstuvwxyz'
c=[]
for i in range (len(t)):
    c.append(t[i]*(i+1))
print(c)

