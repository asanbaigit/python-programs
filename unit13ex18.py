"""
Write a function called base20 that converts a base 10 number to base 20. It should return the result as a 
string of base 20 digits. One way to convert is to ﬁnd the remainder when the number is divided by 20, 
then divide the number by 20, and repeat the process until the number is 0. The remainders are the base 
20 digits in reverse order, though you have to convert them into their letter equivalents."""

from string import ascii_uppercase
A = ascii_uppercase
D = {i: A[i] for i in range(20)}

def base20(n):
    L = []
    while n > 0:
        d = n % 20
        n = n // 20
        L.append(d)
    L.reverse()
    s = ''
    for l in L:
        s = s + D[l]
    return s

n = eval(input('Enter n :'))
print(base20(n))