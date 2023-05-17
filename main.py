
import random

playing = True
card_suits = ('Hearts', 'Spades', 'Clubs', 'Dimonds')
card_ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
deck = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10,
        'queen': 10, 'king': 10, 'ace': 11}


class Cards:
    def __init__(self, suits, ranks):
        self.suit = suits
        self.rank = ranks

    def __repr__(self):
        string = "you have a {ranks} of {suits}".format(ranks=self.rank, suits=self.suit)
        return string

class Deck(Cards):
    def __init__(self):
        self.deck = []
        for suit in card_suits:
            for rank in card_ranks:
                self.deck.append(Cards(suit, rank))

    def __repr__(self):
        string = ''
        for card in self.deck:
            string += ' ' + str(card)
        return string

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __repr__(self):
        string = "You have {card} in your hand, that equals {value}".format(card=self.cards, value=self.value)
        bust = "{card}, you have busted. {value}, {aces}".format(card=self.cards, value=self.value, aces=self.aces)
        if self.value <= 21:
            return string
        else:
            return bust

    def add_card(self, cards):
        self.cards.append(cards)
        self.value += deck[cards.rank]
        if cards.rank == 'ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, chips):
        self.total = 100
        self.chips = chips
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


player_chips = Chips(100)


class take_bet(Chips):
    while True:
        try:
            player_chips.bet = int(input('How many chips would you like to bet\n'))
        except ValueError:
            print('Must be an integer!\n')
        else:
            if player_chips.bet > player_chips.total:
                print("Sorry chips bet cant exced total", player_chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(black_jack_deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's'\n")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands... Dealer is now playing")
            playing = False
        else:
            print("Sorry only enter a 'h' or 'ns'\n")
            continue
        break


def show_some(player, dealer):
    print("\n Dealers hand:")
    print("card hidden")
    print(' ', dealer.cards[1])
    print('\n Players Hand:', *player.cards, player.value, sep='\n')


def show_all(player, dealer):
    print("\n Dealers Hand:", *dealer.cards, sep="\n")
    print("\n Dealers Hand = ", dealer.value)
    print("\n Players Hand:", *player.cards, sep="\n")
    print("\n Players Hand = ", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    player_chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    player_chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    player_chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    player_chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:

    card = Cards(card_suits, card_ranks)
    black_jack_deck = Deck()
    black_jack_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(black_jack_deck.deal())
    player_hand.add_card(black_jack_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(black_jack_deck.deal())
    dealer_hand.add_card(black_jack_deck.deal())

    print('Welcome to Black Jack!')

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)
    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            show_all(player_hand, dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
            show_all(player_hand, dealer_hand)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            show_all(player_hand, dealer_hand)
        else:
            push(player_hand, dealer_hand)
    print('Player winnings stand at ', player_chips.total)
    new_game = input("would you like to play again? Enter 'y' or 'n'\n")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing! ')

        break

