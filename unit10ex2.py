"""
 Write a program that asks the user for a weight in kilograms. The program should convert the weight to 
 kilograms, formatting the result to one decimal place. """

weight = eval(input('Enter the weight in kilograms : '))

print('{:.1f}'.format(weight))
