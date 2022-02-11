import random

# making a deck of cards
number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
suites = [u"\u2663", u"\u2660", u"\u2666", u"\u2665"]
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

# Dealer is a sub-class of player - deals with checking wins, starting new games


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

        else:
            self.is_there_a_winner = True

    def check_for_lose(self, player):
        if int(player.calculate_hand()) > 21:
            print(f"{player.name} Loses")
            self.is_there_a_winner = True

        else:
            pass

        """elif int(player.calculate_hand()) == 21:
            print(f"{player.name} Wins")
            self.is_there_a_winner = True"""

    def new_hand(self, player, dealer):
        player.hand = []
        dealer.hand = []

    def new_game(self):
        another_game = input("Play another round?  y/n:  ")
        if another_game == "y":
            begin_game()
        else:
            pass


# starts a game and makes sure all settings are back to default


def begin_game():
    player.stay = False
    dealer1.stay = False
    dealer1.is_there_a_winner = False
    player.hand = []
    dealer1.hand = []
    dealer1.new_hand(player, dealer1)
    dealer1.deal_cards(player, deck1)
    print(f"{name}'s hand is: " + str(player.hand))
    print("Count: " + str(player.calculate_hand()) + "\n")
    print("\nThe DEALER's hand is: " + str(dealer1.hand))
    print("Count: " + str(dealer1.calculate_hand()) + "\n")


# game mechanics start here


# players turn
def game_mechanics():
    while dealer1.is_there_a_winner == False:
        if player.stay == True and dealer1.stay == True:
            dealer1.check_for_win(player, dealer1)
            dealer1.new_game()

        if player.stay == False:
            hit_stay = input("'hit' or 'stay'?: ")
            if hit_stay == "stay":
                player.stay = True
            elif hit_stay == "hit":
                player.hit(deck1)
                dealer1.check_for_lose(player)
                if dealer1.is_there_a_winner == True:
                    dealer1.new_game()
                else:
                    pass
            else:
                pass
        else:
            pass

    # dealers turn
        if dealer1.stay == False:
            if dealer1.calculate_hand() <= 16:
                dealer1.hit(deck1)
                dealer1.check_for_lose(dealer1)
                if dealer1.is_there_a_winner == True:
                    dealer1.new_game()
            else:
                dealer1.stay = True
        else:
            pass


# while is_there_a_winner == True and the game can start again.
# setting up a game
dealer1 = Dealer("Dealer")
deck1 = Deck(deck)
deck1.shuffle_deck()
name = input("Please input your name: ")
player = Player(name, 100)
print("`~*- BLACKJACK -*~`\n")
print(f"\n Welcome {name}!\n")

begin_game()

game_mechanics()

dealer1.new_game()
