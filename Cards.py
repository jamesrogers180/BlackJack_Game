class Cards:
    def __init__(self, suits, ranks):
        self.suit = suits
        self.rank = ranks

    def __repr__(self):
        string = "you have a {ranks} of {suits}".format(ranks=self.rank, suits=self.suit)
        return string