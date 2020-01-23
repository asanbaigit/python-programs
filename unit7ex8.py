""" Write a program that asks the user for an integer and creates a list that consists of the factors of that 
integer. """

s = eval(input('Enter the number : '))
l = []
for i in range (1,(s+1)):
    if s % i == 0:
        l.append(i)

print (l)

