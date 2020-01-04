"""Write a program that asks the user to enter a string, then prints out each letter of the string doubled and on a
 separate line. For instance, if the user entered HEY, the output would be
 HH
 EE
 YY """

t=input('enter a string ')
for i in range(len(t)):
    print(t[i]*2)
    print()
    
