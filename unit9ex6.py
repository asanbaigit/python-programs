"""
Modify the higher/lower program so tha twhen there is only one guess left,it says 1 guess, not 1 guesses. """

from random import randint
guessesleft = 5
counter = 0
secretnum = randint(1,100)
while guessesleft > 0 :
    guese = eval(input('guess number between 1 and 100 '))
    if guese == secretnum:
        print('You got it')
        break
    guessesleft = guessesleft - 1
    if guese > secretnum and guessesleft > 1:
        print('Lower',' You have',guessesleft,' guesses left')
    elif guese < secretnum and guessesleft > 1:
        print('Higher',' You have',guessesleft,' guesses left')
    elif guese > secretnum and guessesleft == 1:
        print('Lower',' You have',guessesleft,' guess left')
    elif guese < secretnum and guessesleft == 1:
        print('Higher',' You have',guessesleft,' guess left')
    else :
        print('Sorry you could not guess the number')

