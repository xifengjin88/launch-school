class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit