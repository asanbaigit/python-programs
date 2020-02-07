""" Write a function called rectangle that takes two integers m and n as arguments and prints out an m×n box
 consisting of asterisks. Shown below is the output of rectangle(2,4) **** **** """

def rect (n,m):
    for i in range(n):
        print('*'*m)

n = eval(input('enter n:'))
m = eval(input('enter m:'))

rect(n,m)





