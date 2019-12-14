# Write a program that asks the user to enter an angle between −180◦ and 180◦.
# Using an expression with the modulo operator, convert the angle to its
# equivalent between 0◦ and 360◦.



angle = float(input('enter an angle between -180 and 180 '))
if  angle < -180 :
    print ('error!')
elif angle > 180 :
    print ('error!')
elif angle > 0 :
    print (angle ,'degree')
elif angle < 0 :
    print ( 360 + angle, 'degree' )
else :
    print (angle, 'degree')
    


    

              
