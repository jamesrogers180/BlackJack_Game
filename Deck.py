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
