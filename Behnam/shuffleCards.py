import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace' ]

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

rank = random.randrange(0, len(ranks))
suit = random.randrange(0, len(suits))

print(ranks[rank] + " of " + suits[suit])