import random

def deck():
    suites=["Clubs","Diamonds","Spades", "Hearts"]
    numbers=[2,3,4,5,6,7,8,9,10] + ["Jack","Queen","King","Ace"]
    full_deck = [[number] + [suite] for number in numbers for suite in suites]
    return full_deck

def deal_hands():
    player_hand.append(full_deck.pop())
    dealer_hand.append(full_deck.pop())
    player_hand.append(full_deck.pop())
    dealer_hand.append(full_deck.pop())

def hit(player):
    player.append(full_deck.pop())


def calculate_hand(hand):
    values=[]
    for card in hand:
        if card[0] == "King" or card[0] == "Queen" or card[0] == "Jack":
            values.append(10)
        elif card[0] == "Ace":
            values.append(11)
        else:
            values.append(card[0])
        
    return (sum(values))


def show_hand(hand, person):
    print("{} cards are: \n".format(person))
    for card in hand:
        print("The " + str(card[0]) + " of " + str(card[1]) + "\n")


def main():

    print("Welcome to BlackJack")
    print("The dealer is now going to deal your hand... \n")
    deal_hands()
    show_hand(player_hand, "Your")
    print("You're total is: " + str(calculate_hand(player_hand)) + "\n")
    show_hand(dealer_hand, "The Dealer")
    print("The Dealers total is: " + str(calculate_hand(dealer_hand))+ "\n")
    
    while calculate_hand(player_hand) <= 21 or calculate_hand(dealer_hand) <= 21:
        hit_stay = input("Would you like to 'hit' or 'stay': ")
        if hit_stay != 'hit' or hit_stay != 'stay':
            print("Please choose a valid option: 'hit' or 'stay'")
            pass
        if hit_stay == "hit":
            hit(player_hand)
            show_hand(player_hand, "Your")
            print("You're total is: " + str(calculate_hand(player_hand)))
        if hit_stay == "stay":
            continue
            
        if calculate_hand(dealer_hand) < 17:
            hit(dealer_hand)
            show_hand(dealer_hand, "The Dealer")
            print("The Dealers total is: " + str(calculate_hand(dealer_hand)))
        else:
            pass
#print("Your cards total to: " + str(total))

full_deck = deck() * 4
random.shuffle(full_deck)
player_hand = []
dealer_hand = []

main()



