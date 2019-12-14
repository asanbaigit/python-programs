"""A year is a leap year if it is divisible by 4, except that years divisible
by 100 are not leap years unless they are also divisible by 400. Ask the user
to enter a year, and, using the // operator, determine how many leap years
there have been between 1600 and that year. """

answer = int(input(' Enter a year between 1600 and 2600 '))

if answer < 1600 :
        print (' error you should Enter a year between 1600 and 2600 ')
elif answer%4!=0:
    print(answer,' it is a common year ')
elif answer%100==0 and answer%400!=0:
    print (answer, ' it is a common year ')
else:
    print (answer, ' it is a leap year ')

print ('*************')
counter = 0
for i in range (1600,answer+1):
    
    if i%100==0 and i%400!=0:
        print (i,' it is a common year ',end='')
    elif i%4==0 :
        counter = counter + 1
        print ((i),' leap year ',end='')
 
        
print ('*************')
print ('*************')
print ('Between 1600 and ', answer,' there are ',counter,' leap years ')










    

    

    
             
