from unit14ex7Cards import Card
from unit14ex7Cards import Standard_deck
'''
card1 = Card(6, 'Hearts')
print(card1)

card2 = Card(14, 'Diamonds')
print(card2)
'''

deck = Standard_deck()
deck.shuffle()
L1 = deck.cards[:len(deck.cards)//2]
p1_deck = Standard_deck(L1)
#print('------------p1 decks---------------')
#print(p1_deck)
L2 = deck.cards[len(deck.cards)//2:]
p2_deck = Standard_deck(L2)
#print('------------p2 decks---------------')
#print(p2_deck)

while p1_deck.hasCard() and p2_deck.hasCard():
    card1 = p1_deck.nextCard()
    card2 = p2_deck.nextCard()
    if card1.compare(card2) > 0:
        print(card1.__str__(), 'of p1 is bigger than', card2.__str__())
        p1_deck.insertCards(card2, card1)
    elif card1.compare(card2) < 0:
        print(card2.__str__(), 'of p2 is bigger than', card1.__str__())
        p2_deck.insertCards(card1, card2)
    else:
        print('dropping...', card1.__str__())
        print('dropping...', card2.__str__())

if not p1_deck.hasCard():
    print('p2 wins')
else:
    print('p1 wins')