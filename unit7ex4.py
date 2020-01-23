"""
Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the
 list that are greater than 10 with 10. """

l = [1,2,3,4,5,6,7,8,9,10,11,12]

for  i in range (len(l)):
    if l[i] > 10 :
        l[i] = 10
print (l)