""" Write a simple quiz game that has a list of ten questions and a list of answers to those questions. The game 
should give the player four randomly selected questions to answer. It should ask the questions one-by-one, and tell the
player whether they got the question right or wrong. At the end it should print out how many out of four they got 
right"""

from random import choice
from random import sample

q = ['2+2', 'cap of GB','3+3','4+4','cap of Fr','1+1','do you love python','altyn bro']
a = ['4','london','6','8','paris','2','yes','tuura']
c = 0
for z in range (4):
    x = choice(q)
    print(x)
    index = q.index(x)
    s =  input('enter the answer ')
    if s == (a[index]):
        print('correct')
        c = c + 1
    else:
        print('wrong')
print ('you have ', c,' correct answers')