import random

# making a deck of cards
number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
suites = ["Clubs", "Spades", "Diamonds", "Hearts"]
deck = [[x, y] for x in number for y in suites]

# deck of cards as a class


class Deck:

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return str(self.cards)

    def deal_card(self):
        pick = self.cards.pop()
        return pick

    def shuffle_deck(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name, money=0):
        self.hand = []
        self.money = money
        self.name = name
        self.stay = False

    def hit(self, deck):
        self.hand.append(deck.deal_card())
        print(f"{self.name}'s hand is: " + str(self.hand))
        print("Count: " + str(self.calculate_hand()) + "\n")

    def staying(self):
        self.stay = True

    def calculate_hand(self):
        total = 0
        for card in self.hand:
            if card[0] == 'J':
                total += 10
            elif card[0] == 'Q':
                total += 10
            elif card[0] == 'K':
                total += 10
            elif card[0] == 'A':
                total += 11
            else:
                total += card[0]

        return total

    def show_hand(self):
        for card in self.hand:
            return str(card[0]) + " of " + str(card[1])


class Dealer(Player):
    def __init__(self, name, money=0):
        super().__init__(name)
        self.hand = []
        self.is_there_a_winner = False

    def deal_cards(self, player, deck):
        player.hand.append(deck.deal_card())
        player.hand.append(deck.deal_card())
        self.hand.append(deck.deal_card())
        self.hand.append(deck.deal_card())

    def check_for_win(self, player, dealer):
        if int(player.calculate_hand()) > 21:
            print("You Lose")
            self.is_there_a_winner = True
            pass

        elif int(dealer.calculate_hand()) > 21:
            print("You win")
            self.is_there_a_winner = True
            pass

        elif int(dealer.calculate_hand()) == 21:
            print('You Lose')
            self.is_there_a_winner = True
            pass

        elif int(player.calculate_hand()) == 21:
            print("You Win")
            self.is_there_a_winner = True
            pass

        elif int(player.calculate_hand()) > int(dealer.calculate_hand()):
            print("You Win")
            self.is_there_a_winner = True
            pass

        elif int(dealer.calculate_hand()) > int(player.calculate_hand()):
            print("You Lose")
            self.is_there_a_winner = True
            pass

    def check_for_lose(self, player):
        if int(player.calculate_hand()) > 21:
            print("You Lose")
            self.is_there_a_winner = True

        elif int(player.calculate_hand()) == 21:
            print("You Win")
            self.is_there_a_winner = True

        else:
            pass

    def new_hand(self, player, dealer, deck):
        player.hand = []
        dealer.hand = []
        begin_game()


def begin_game():
    dealer1.deal_cards(player1, deck1)
    print(f"{name}'s hand is: " + str(player1.hand))
    print("Count: " + str(player1.calculate_hand()) + "\n")

    print("\nThe DEALER's hand is: " + str(dealer1.hand))
    print("Count: " + str(dealer1.calculate_hand()) + "\n")


dealer1 = Dealer("Dealer")
deck1 = Deck(deck)
deck1.shuffle_deck()
print("\nWelcome to Blackjack!\n")
name = input("Please input your name: ")
player1 = Player(name, 100)
print(f"\n Welcome {name}!  You will have $100 to begin with.\n")

begin_game()
while dealer1.is_there_a_winner == False:
    if player1.stay == False and dealer1.stay == False:
        hit_stay = input("'hit' or 'stay'?: ")
        if hit_stay == "stay":
            player1.stay = True
        elif hit_stay == "hit":
            player1.hit(deck1)
            dealer1.check_for_lose(player1)
            if dealer1.is_there_a_winner == True:
                break
        if dealer1.calculate_hand() < 16:
            dealer1.hit(deck1)
            dealer1.check_for_lose(dealer1)
        elif dealer1.calculate_hand() == 21:
            dealer1.stay == True
        else:
            pass

    elif player1.stay == True or dealer1.stay == False:
        if dealer1.calculate_hand() < 16:
            dealer1.hit(deck1)
            dealer1.check_for_lose(dealer1)
        if dealer1.calculate_hand() >= 16:
            dealer1.stay == True
            dealer1.check_for_win(player1, dealer1)

    elif player1.stay == True and dealer1.stay == True:
        dealer1.checker_for_win(player1, dealer1)
