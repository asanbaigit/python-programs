""" Write a program that allows the user to enter ﬁve numbers (read as strings). Create a string that consists 
of the user’s numbers separated by plus signs. For instance, if the user enters 2, 5, 11, 33, and 55, then 
the string should be '2+5+11+33+55'. """
"""
r = ''
for i in range (1):
    r = r + (input('enter number '))
    for j in range(4):
        r = r + '+' + (input('enter number '))
print(r)"""

### solution by teacher 

nams = []
for i in range(5):
    nams.append(input('enter the number '))
print('+'.join(nams))