""" Write a program that rotates the elements of a list so that the element at the ﬁrst index moves to the second index, 
the element in the second index moves to the third index, etc., and the element in the last index moves to the ﬁrst index.
"""
l=eval(input('enter a list '))
for i in range (len(l)):
    print((l[i:]) + (l[:i]))
    