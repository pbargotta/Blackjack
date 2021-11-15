import random


class Player:
    def __init__(self):
        self.winner = False
        self.loser = False
        self.ace = None
        self.deck = []

    def acevalue(self):
        self.ace = int(input("Would you like your ace to count as a '1' or an '11'? "))


# gives each card 4 suits - representing spades, clubs, hearts and diamonds
class Card:
    def __init__(self):
        self.suitsremaining = 4

    def removesuit(self):
        self.suitsremaining -= 1


# initialises the players deck with their first two cards and prints them out to the players
def init_player_decks():
    for player_deck in [player_1.deck, player_2.deck]:
        for _ in range(2):
            card_drew = random.choice(deck_options)
            player_deck.append(card_drew)

    print("Player 1 your starting cards are: ", end="")
    print(*player_1.deck, sep=", ")
    for check_for_ace in player_1.deck:
        if check_for_ace == "Ace":
            player_1.acevalue()
    print(f"This gives you a total of: {deck_value(player_1.deck)}\n")

    print("Player 2 your starting cards are: ", end="")
    print(*player_2.deck, sep=", ")
    for check_for_ace in player_2.deck:
        if check_for_ace == "Ace":
            player_2.acevalue()
    print(f"This gives you a total of: {deck_value(player_2.deck)}\n")


# converts the players hand into its corresponding numerical value
def deck_value(player_deck):
    value = 0
    for card in player_deck:
        if card.isdigit():
            value += int(card)
        elif card in ["Jack", "Queen", "King"]:
            value += 10
        elif card == "Ace":
            if player_deck == player_1.deck:
                value += player_1.ace
            elif player_deck == player_2.deck:
                value += player_2.ace

    return value


# deals a random card from the deck and removes the chance of getting a single type of card more than 4 times to
# represent each suit and prints the players current cards using the correct article as well as their current hand
def deal_new_card(player):
    # prints the players current cards and uses the correct article needed
    def print_card_drew(card):
        if card in ["Ace", "8"]:
            print(f"Player {player}, you drew an {card}!")
        else:
            print(f"Player {player}, you drew a {card}!")

        if player == "1":
            if card_drew == "Ace":
                player_1.acevalue()
            print("Player 1, your cards are now: ", end="")
            print(*player_1.deck, sep=", ")
            print(f"Your total is now: {deck_value(player_1.deck)}\n")
        elif player == "2":
            if card_drew == "Ace":
                player_1.acevalue()
            print("Player 2, your cards are now: ", end="")
            print(*player_2.deck, sep=", ")
            print(f"Your total is now: {deck_value(player_2.deck)}\n")

    card_drew = random.choice(deck_options)

    if player == "1":
        player_1.deck.append(card_drew)
    elif player == "2":
        player_2.deck.append(card_drew)

    deck[card_drew].removesuit()
    if deck[card_drew].suitsremaining == 0:
        del deck[card_drew]

    print_card_drew(card_drew)


# checks if the deck total is equal to or more than 21 and checks if any one has 5 cards and determines after 7 rounds
# who has the hand closest to 21 to award the winner
def check_for_winner(player):
    deck_total = deck_value(player.deck)

    if len(player.deck) == 5:
        player.winner = True
    elif deck_total == 21:
        player.winner = True
    elif deck_total > 21:
        player.loser = True


def run_game():
    rounds_played = -1

    print("Welcome to Blackjack!\n")
    init_player_decks()

    while not player_1.winner and not player_2.winner and not player_1.loser and not player_2.loser:
        # checks after 7 rounds of dealing the deck totals of each player and the closest to 21 is the winner
        rounds_played += 1
        if rounds_played == 7:
            if deck_value(player_1.deck) > deck_value(player_2.deck):
                player_1.winner = True
                continue
            elif deck_value(player_1.deck) < deck_value(player_2.deck):
                player_2.winner = True
                continue

        for player in ["1", "2"]:
            user_choice = input(f"Player {player}, would you like to hit or stand? ").lower()
            if user_choice == "hit":
                deal_new_card(player)

            if player == "1":
                check_for_winner(player_1)
                if player_1.winner or player_1.loser:
                    break
            elif player == "2":
                check_for_winner(player_2)
                if player_2.winner or player_2.loser:
                    break

    if player_1.winner:
        print("Player 1 won!")
    elif player_1.loser:
        print("Player 1 lost!")
    elif player_2.winner:
        print("Player 2 won!")
    elif player_2.loser:
        print("Player 2 lost!")


player_1 = Player()
player_2 = Player()
deck = {"Ace": Card(),
        "2": Card(),
        "3": Card(),
        "4": Card(),
        "5": Card(),
        "6": Card(),
        "7": Card(),
        "8": Card(),
        "9": Card(),
        "10": Card(),
        "Jack": Card(),
        "Queen": Card(),
        "King": Card()}
deck_options = list(deck.keys())

run_game()
