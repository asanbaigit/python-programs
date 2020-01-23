""" Write a program that asks the user to enter a length in feet. The program should then give the user the 
option to convert from feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers. Say if 
the user enters a 1, then the program converts to inches, if they enter a 2, then the program converts to yards, 
etc. While this can be done with if statements, it is much shorter with lists and it is also easier to add new 
conversions if you use lists. """

l = eval(input('Enter a length in feet '))
a = eval(input('To convert feet into inches enter 1, to yards enter 2, to miles enter 3, to mm 4, to cm 5, to m 6, to km 7 :'))

y = [(l*2),(l/3),(l/5280),(l*304.8),(l*30.48),(l/3.281),(l/3281)]
z = ['inches','yards','miles','millimeters','centimeters','meters','kilometers']

print('It is: ',(y[a-1]),z[a-1])