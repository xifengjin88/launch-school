from card_game import Card
from random import shuffle, choice


class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self, cards=None):
        if not cards:
            cards = []
        self._cards = cards if cards else self._initialize()

    def _initialize(self):
        cards = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]
        shuffle(cards)
        return cards

    def draw(self):
        if len(self._cards) == 0:
            self._cards = self._initialize()

        return self._cards.pop()


if __name__ == '__main__':
    deck = Deck()
    drawn = []
    for _ in range(52):
        drawn.append(deck.draw())

    count_rank_5 = sum([1 for card in drawn if card.rank == 5])
    count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

    print(count_rank_5 == 4)  # True
    print(count_hearts == 13)  # True

    drawn2 = []
    for _ in range(52):
        drawn2.append(deck.draw())

    print(drawn != drawn2)  # True (Almost always).
