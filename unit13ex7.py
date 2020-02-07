"""
 Write a function that takes an integer n and returns a random integer with exactly n digits. For instance,
 if n is 3, then 125 and 593 would be valid return values, but 093 would not because that is really 93, which
  is a two-digit number. """

from random import randint

def rand_dig(n):
    n_l = 10 ** n-1
    n_f = 10 ** (n-1)
    if n_f == 1:
        n_f = 0
    return randint(n_f,n_l)

num = eval(input('enter the num: '))
print(rand_dig(num))