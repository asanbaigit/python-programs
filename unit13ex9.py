"""
Write a function called factors that takes an integer and returns a list of its factors. """

def factors (n):
    return [i for i in range (1,n) if n % i == 0]

num = eval (input('Enter the num :'))

print(factors(num))
