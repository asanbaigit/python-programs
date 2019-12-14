
#Write a program that generates and prints 50 random
#integers, each between 3 and 6.


from random import randint

for i in range (1,51):
    x = randint(3,6)
    print (i,'A random number between 3 and 6: ', x)
    
    
