## Prime number
"""num=eval(input('Enter a number '))
flag=1
for i in range (2,num):
    if num % i ==0:
        flag=0
if flag ==1:
    print(num,' is a prime')
else:
    print(num,' is not a prime')

## Finding if number is prime number"""

num=eval(input('Enter a number '))
c=0
for i in range (1,num+1):
    if num % i == 0:
        c=c+1
if c == 2 :
    print(num,' is a prime')
else:
    print(num,' is not a prime')
