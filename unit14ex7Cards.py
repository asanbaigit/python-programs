import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        names = ['Jack' ,'Queen' , 'King', 'Ace']
        if self.value <= 10:
            return ' {} of {} ' .format(self.value, self.suit)
        else:
            return ' {} of {} ' .format(names[self.value-11], self.suit)

    def compare(self, other):
        if self.value == other.value:
            return 0
        elif self.value > other.value:
            return 1
        else:
            return -1

class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards

    def nextCard(self):
        return self.cards.pop(0)

    def hasCard(self):
        return len(self.cards)>0
    
    def size(self):
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def insertCards(self, card1, card2):
        self.cards.append(card1)
        self.cards.append(card2)

class Standard_deck(Card_group):
    def __init__(self, cards=[]):
        if len(cards) == 0:
            self.cards = []
            for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                for v in range(2,15):
                    self.cards.append(Card(v, s))
        else:
            self.cards = cards

    def __str__(self):
        return '\n'.join([card.__str__() for card in self.cards])