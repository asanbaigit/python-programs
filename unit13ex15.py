"""
Write a function called root that is given a number x and an integer n and returns x1/n. In the function 
deﬁnition, set the default value of n to 2. """

def root (x, n=2):
    return x**1//n

x = eval(input('X :'))
n = eval(input('n :'))

print(root(x,n))
