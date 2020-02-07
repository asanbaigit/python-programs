"""
 Write a function called sum_digits that is given an integer num and returns the sum of the digits of num. """

def sum_digits (num):
    result = 0
    while num > 0:
        d = num % 10
        num = num // 10
        result = result + d
    return result

n = eval(input('enter num: '))
r = sum_digits(n)
print('sum of digits is =', r)
    

