"""
Write a program that asks the user to enter a password. If the user enters the right password, the program
should tell them they are logged in to the system. Otherwise, the program should ask them to reenter the
password. The user should only get ﬁve tries to enter the password, after which point the program should 
tell them that they are kicked off of the system """
s = 5
pw1 = 'simsim'
c = 0 
while c < 5:
    pw = (input('Enter the password : '))
    c = c + 1 
    s = s - 1
    if pw == pw1:
        print('You are logged in to the system')
        break
    elif c == 5:
        print('Password is wrong! You are kicked off of the system.')
    else :
        print('Password is wrong! Please re enter password, you have left', s , 'more tries')




