"""Write a program that asks the user to enter a length
 in centimeters. If the user enters a negative length,
 the program should tell the user that the entry is invalid.
 Otherwise, the program should convert the length to inches
 and print out the result. There are 2.54 centimeters in an inch."""

l=int(input(' enter the lenght in cm '))
if l < 0:
     print('the entry is invalid')
else:
    print('length in inches is ',l*2.54)