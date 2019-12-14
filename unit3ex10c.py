# Write a program that asks the user to enter a power and how many
# digits they want. Find the last that many digits of 2 raised to
# the power the user entered

power = int(input('enter a power '))
digits = int(input('enter a number of digits '))
x=2
y = str(x**power)
print (y)
print ((y [-(digits):]))


    
