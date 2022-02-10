import random 

def shuffle_deck():
    shuffled_deck = deck[:]
    random.shuffle(shuffled_deck)
    return shuffled_deck

figures = [str(x) for x in (tuple(range(2, 11)) + ("J", "Q", "K", "A"))]
suits = ["♠", "♥", "♦", "♣"]
deck = [figure+suit for figure in figures for suit in suits]



