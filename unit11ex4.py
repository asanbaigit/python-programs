"""Write a program that uses a dictionary that contains ten user names and passwords. The program should ask 
the user to enter their user name and password. If the user name is not in the dictionary,the program should 
indicate that the person is not a valid user of the system. If the user name is in the dictionary,but the user 
does not enter the right password,the program should say that the password is invalid. If the password is correct
then the program should tell the user that they are now logged in to the system. """

D = {'aza':11,'ali':12,'adi':13}

user = input('Enter the user name : ')

flag = False

if user not in D :
    print('This is not valid user')

else :
    pasw = eval(input('enter pasw '))
    for z in D:
        if z == user and D[z] == pasw:
            flag = True
if flag:
    print ('Loged in')
else :
    print('try again')