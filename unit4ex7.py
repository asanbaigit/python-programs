"""Write a program that asks the user for two numbers and prints Close if the numbers are within .001 
of each other and Not close otherwise"""

num1=float(input('Enter a number '))
num2=float(input('Enter a number '))
if abs(num1-num2)<0.001:
    print('Close')
else:
    print('Not close')