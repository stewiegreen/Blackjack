import random

class Dealer:
    
    pass

class Player:
    pass


def deck():
    suites=["Clubs","Diamonds","Spades", "Hearts"]
    numbers=[2,3,4,5,6,7,8,9,10] + ["Jack","Queen","King","Ace"]
    full_deck = [[number] + [suite] for number in numbers for suite in suites]
    return full_deck

full_deck = deck()

random.shuffle(full_deck)

print(full_deck[51][0])
