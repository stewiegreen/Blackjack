import random

class Player:
    def __init__(self, name, hand = None, value = 0):
        self.name = name
        self.hand = hand
        self.value = value
        self.done == False
        self.bust == False 
        self.hand = []
       
        value = 0

    def is_bust(self):
        if self.card_value() > 21:
            self.done = True

    def player_stay(self):
        self.done = True

    def is_done(self):
        return self.done
    
    def get_name(self):
        return self.name
    
    def card_value(self):
        values=[]
        for card in self.hand:
            if card[0] == "King" or card[0] == "Queen" or card[0] == "Jack":
                values.append(10)
            elif card[0] == "Ace":
                values.append(11)
            else:
                values.append(card[0])
                
        if sum(values) > 21:
            for card in self.hand:
                if card[0] == 'Ace':
                  values.append(-10)
        
        return (sum(values))
    

    def hit(self, card):
        self.hand.append(card)

    def show_hand(self):
        print("{0}'s cards are: \n".format(self.name))
        for card in self.hand:
            print(str(card[0]) + " of " + str(card[1]) + "\n")
    
    def num_cards(self):
        return len(self.hand)
    
class Dealer(Player):
    def __init__(self, name, hand = None, value = 0):
        super().__init__(name)
        self.deck = []
    
    
    def cards(self, n):
        suites=["Clubs","Diamonds","Spades", "Hearts"]
        numbers=[2,3,4,5,6,7,8,9,10] + ["Jack","Queen","King","Ace"]
        self.deck = [[number] + [suite] for number in numbers for suite in suites]
        return (self.deck * n)
    
    def dealer_done(self):
        return self.done

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_card(self, Player):
        Player.hit(self.deck.pop())

    def hit_or_stay(self, player, dealer):
        if player.card_value() > 21:
            
            print("Bust!  Sorry, you lose")
            pass
        hit_stay = input("{}, Hit or Stay (h/s):".format(player.get_name()))
        if hit_stay == 's':
            player.player_stay()
            pass
        
        if hit_stay == 'h':
            dealer.deal_card(player)
            player.show_hand()
            pass
    
    def dealer_turn(self, dealer):
        if dealer.card_value() <= 17:
            dealer.deal_card(dealer)
            dealer.show_hand()
        if dealer.card_value() > 17 and dealer.card_value() <= 21:
            print("Dealer Stays")
            self.done = True
            pass
        if dealer.card_value() > 21:
            self.done = True
            pass
    


def main():
    persons = []
    dealer = Dealer("dealer")
    
    num_players = input("Welcome to Blackjack! \n How many will be playing (upto 2)?: ")
    if num_players == '1' or num_players == '2':
        for i in range(int(num_players)):
            person = input("Enter your name: ")
            person = Player(person)
            persons.append(person)
    else:
        print("sorry, that's not a valid answer")
        main()
    
    dealer.cards(4)

    dealer.shuffle_deck()
    
    for person in persons:
        dealer.deal_card(person)
        
    dealer.deal_card(dealer)

    for person in persons:
        dealer.deal_card(person)
        person.show_hand()

    dealer.deal_card(dealer)

    dealer.show_hand()

    print(dealer.card_value())
    while dealer.done == False:
        for person in persons: 
            if person.done == True:
                print(person.name + " has stayed, next player.")
                continue
            if person.card_value() < 21:
                dealer.hit_or_stay(person, dealer)
                print(person.card_value())
            if person.card_value() > 21:
                person.is_bust()
        
        dealer.dealer_turn(dealer)
    
    for person in persons:
        if dealer.card_value() > 21 and person.card_value() <= 21:
            print("Dealer busts!  " + person.name + " wins!")
        
        if person.card_value() <= 21 and person.card_value() > dealer.card_value():
            print(person.name + " wins!")
        
        if dealer.card_value() == person.card_value():
            print("draw")

        else:
            print(person.name + ", you lose.")

        
main()

#def isdone(): function that sets isdone as True when a player stays or isbust 
# 
#def isbust(): looking at the deck of the most recent player and determines if they're bust - activates isdone()
#  

#human: bust and done

#dealer: dust and done