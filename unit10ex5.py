"""
Use the following two lists and the format method to create a list of card names in the format card value of suit
name (for example, 'Two of Clubs'). """
from random import choice
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
'Jack', 'Queen', 'King', 'Ace']


for v in values:
    for s in suits:
        print('{:10s} of {:>10s}'.format(v,s))



