import Deck
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
