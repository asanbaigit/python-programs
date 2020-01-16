""" Write a simple quiz game that has a list of ten questions and a list of answers to those questions. The game 
should give the player four randomly selected questions to answer. It should ask the questions one-by-one, and tell the
player whether they got the question right or wrong. At the end it should print out how many out of four they got 
right"""

from random import choice
from random import sample

q = ['2+2=?', 'capital of GB?','3+3=?','4+4=?','capital of Fr?','1+1=?','do you love python?','is altyn bro?']
a = ['4','london','6','8','paris','2','yes','yes']
c = 0
d = []
f = 0
while f < 4: # for i in range bolboi koydu
    x = choice(q)
    if x not in d:
        f = f+1
        d.append(x)
        print(x)
        index = q.index(x)
        s =  input('enter the answer ')
        if s == (a[index]):
            print('correct')
            c = c + 1
        else:
            print('wrong')
        print('---------------')
print ('you have ', c,' correct answers')