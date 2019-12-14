""" Write a program that asks the user to enter a weight in kilograms.
The program should convert it to pounds, printing the answer rounded
to the nearest tenth of a pound. """

weight = int(input(' Enter a weight in kilograms '))

            
# pounds = kg / 0.45359237

print (weight / 0.45359237, ' weight in pounds ')

print ((round(weight/0.45359237,-1)), ' rounded weight in pounds')

print ((round(weight/0.45359237, 2)), ' rounded weight in pounds')
