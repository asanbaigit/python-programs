"""
A good program will make sure that the data its users enter is valid. Write a program that asks the user for a
 weight and converts it from kilograms to pounds. Whenever the user enters a weight below 0,
 the program should tell them that their entry is invalid and then ask them again to enter a weight. 
 [Hint: Use a while loop, not an if statement]."""

 # kg/ 0.45359237 = pounds

""" this option is not so much good
a =  100 
while a > 0:
    a = eval(input('Enter a weight in kg: '))
    print('In pounds that is', a/0.45359237)
else :
    print('entry is invalid please re enter the weight')"""

#
""" This option is better
n = eval(input('enter w in kg '))
while n < 0:
    print('input is invalid')
    n = eval(input('enter w in kg '))
print('in pounds = ', n*2.205)
"""
# This option is also better 
n = 0
while True :
    n = eval(input('enter w in kg '))
    if n >= 0 :
        break
    print('input is invalid')
print('in pounds = ', n*2.205)
