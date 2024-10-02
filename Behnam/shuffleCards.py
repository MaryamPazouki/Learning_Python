import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace' ]

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# rank = random.randrange(0, len(ranks))
# suit = random.randrange(0, len(suits))
deck = []
for suit in suits:
    for rank in ranks:
        card = rank + ' of ' + suit
        deck += [card]
for i in range(len(deck)):
    r = random.randrange(0, i + 1)
    temp = deck[i]
    deck[i] = deck[r]
    deck[r] = temp
for i in deck:
    print(i)