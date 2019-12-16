"""Generate a random number between 1 and 10. Ask the user to guess the number and print a message based on 
whether they get it right or not"""

import random
from random import randint

guess=int(input('guess a number between 1 and 10 '))

generate=randint(1,10)
print('My number is ',generate)

if guess==generate:
    print('You got it right')
else:
    print('You could not guess it')