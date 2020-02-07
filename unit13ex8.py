"""
Write a function called number_of_factors that takes an integer and returns how many factors the number has. """

def factors (n):
    return len( [i for i in range (1,n) if n % i == 0] )

num = eval (input('Enter the num :'))

print(factors(num))
