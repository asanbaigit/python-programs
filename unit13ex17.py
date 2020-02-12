"""
(a) Write a function called primes that is given a number n and returns a list of the ﬁrst n primes. 
Let the default value of n be 100. 
(b) Modify the function above so that there is an optional argument called start that allows the list to start 
at a value other than 2. The function should return the ﬁrst n primes that are greater than or equal to start. 
The default value of start should be 2. """
#a
'''
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def primes(n = 100):
    for i in range (2,n+1):
        if is_prime(i):
            print(i)

p = eval (input('enter n :'))
primes (p)
'''
#b

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def primes(s = 2, n = 100):
    for i in range (s,n+1):
        if is_prime(i):
            print(i)

s = eval (input('enter s :'))
p = eval (input('enter n :'))
primes (s,p)

