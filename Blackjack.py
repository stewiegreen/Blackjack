import random

def deck():
    suites=["Clubs","Diamonds","Spades", "Hearts"]
    numbers=["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]
    full_deck = []

    for suite in suites:
        for number in numbers:
            full_deck.append(number + " " + suite)
    return full_deck

full_deck = deck()

random.shuffle(full_deck)

print(full_deck)