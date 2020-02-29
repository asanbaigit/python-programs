"""
s = 'insert 0 5'

c = s.split()

print(c)
L = []
def f('x'):

    L = 'L'+'.'+c[0]+'('+c[1]+','+c[2]+')'

print(exec(f('c')))
"""

def simlearrayfunc(ar,n):
    L = list((ar.split(' ')))
    sum = 0
    for i in L:
        sum = sum + int(i)
    return sum

n = input('enter the size of array')
ar = input('enter the arrays elements by space')

print(simlearrayfunc(ar,n))