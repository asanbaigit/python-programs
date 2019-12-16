""" Write a program that asks the user how many credits they have taken. If they have taken 23 or less, 
print that the student is a freshman. If they have taken between 24 and 53, print that they are a sophomore. 
The range for juniors is 54 to 83, and for seniors it is 84 and over"""

credit=int(input('Enter the number of credits you have taken '))
if credit<=23:
    print('You are a Freshman')
elif 24<=credit<=53:
    print('You are a Sophomore')
elif 54<=credit<=83:
    print('You are Junior')
else:
    print('You are Senior') 
