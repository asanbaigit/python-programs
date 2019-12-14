# Write a program that asks the user for an hour between 1 and 12 and
# for how many hours in the future they want to go. Print out what
# the hour will be that many hours into the future. An example is shown below.

# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 o'clock

answer1 = int(input(' enter hour between 1 and 12 '))
answer2 = int(input(' How many hours ahead? '))
newhour = answer1+answer2
if newhour > 12 :
    print ('New hour is ',newhour%12)
else :
    print (newhour)
    


