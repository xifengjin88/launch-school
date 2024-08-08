# Include Card and Deck classes from the last two exercises.

from deck_of_cards import Deck
from card_game import Card


def create_sequence():
    sequence = ['Ace', 'King', 'Queen', 'Jack', 10, 9, 8, 7, 6, 5, 4, 3, 2]
    return [sequence[i: i + 5] for i in range(len(sequence) - 4)]


class PokerHand:
    SEQUENCES = create_sequence()

    def __init__(self, deck):
        self._deck = deck
        self._cards = [self._deck.draw() for _ in range(5)]

    def print(self):
        for card in self._cards:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
            return "High card"

    def _sames_suit(self):
        suits = [card.suit for card in self._cards]
        return len(set(suits)) == 1

    def _is_royal_flush(self):
        if not self._sames_suit():
            return False
        ranks = [card.rank for card in self._cards]
        for rank in [10, 'Jack', 'Queen', 'King', 'Ace']:
            if rank in ranks:
                ranks.remove(rank)
        return len(ranks) == 0

    def _is_sequence(self):
        cards = sorted(self._cards)
        ranks = [card.rank for card in cards]
        for sequence in PokerHand.SEQUENCES:

            if ranks == sequence or ranks == sequence[::-1]:
                return True
        return False

    def _is_straight_flush(self):
        if not self._sames_suit():
            return False
        return self._is_sequence()

    def _one_of_a_kind(self, kinds, count):
        ranks = [card.rank for card in self._cards]
        unique_ranks = set(ranks)
        if len(unique_ranks) != count:
            return False
        for rank in unique_ranks:
            if sorted([ranks.count(r) for r in unique_ranks]) == sorted(kinds):
                return True
        return False

    def _is_four_of_a_kind(self):
        return self._one_of_a_kind([4, 1], 2)

    def _is_full_house(self):
        return self._one_of_a_kind([3, 2], 2)

    def _is_flush(self):
        return not self._is_sequence() and self._sames_suit()

    def _is_straight(self):
        return self._is_sequence() and not self._sames_suit()

    def _is_three_of_a_kind(self):
        return self._one_of_a_kind([3, 1, 1], 3)

    def _is_two_pair(self):
        return self._one_of_a_kind([2, 2, 1], 3)

    def _is_pair(self):
        return self._one_of_a_kind([2, 1, 1, 1], 4)


if __name__ == '__main__':
    hand = PokerHand(Deck())
    hand.print()
    print(hand.evaluate())
    print()


    # Adding TestDeck class for testing purposes

    class TestDeck(Deck):
        def __init__(self, cards):
            super().__init__(cards)
            self._deck = cards


    hand = PokerHand(
        TestDeck(
            [
                Card("Ace", "Hearts"),
                Card("Queen", "Hearts"),
                Card("King", "Hearts"),
                Card("Jack", "Hearts"),
                Card(10, "Hearts"),
            ]
        )
    )
    print(hand.evaluate() == "Royal flush")

    hand = PokerHand(
        TestDeck(
            [
                Card(8, "Clubs"),
                Card(9, "Clubs"),
                Card("Queen", "Clubs"),
                Card(10, "Clubs"),
                Card("Jack", "Clubs"),
            ]
        )
    )
    print(hand.evaluate() == "Straight flush")

    hand = PokerHand(
        TestDeck(
            [
                Card(3, "Hearts"),
                Card(3, "Clubs"),
                Card(5, "Diamonds"),
                Card(3, "Spades"),
                Card(3, "Diamonds"),
            ]
        )
    )
    print(hand.evaluate() == "Four of a kind")

    hand = PokerHand(
        TestDeck(
            [
                Card(3, "Hearts"),
                Card(3, "Clubs"),
                Card(5, "Diamonds"),
                Card(3, "Spades"),
                Card(5, "Hearts"),
            ]
        )
    )
    print(hand.evaluate() == "Full house")

    hand = PokerHand(
        TestDeck(
            [
                Card(10, "Hearts"),
                Card("Ace", "Hearts"),
                Card(2, "Hearts"),
                Card("King", "Hearts"),
                Card(3, "Hearts"),
            ]
        )
    )
    print(hand.evaluate() == "Flush")

    hand = PokerHand(
        TestDeck(
            [
                Card(8, "Clubs"),
                Card(9, "Diamonds"),
                Card(10, "Clubs"),
                Card(7, "Hearts"),
                Card("Jack", "Clubs"),
            ]
        )
    )
    print(hand.evaluate() == "Straight")

    hand = PokerHand(
        TestDeck(
            [
                Card(3, "Hearts"),
                Card(3, "Clubs"),
                Card(5, "Diamonds"),
                Card(3, "Spades"),
                Card(6, "Diamonds"),
            ]
        )
    )
    print(hand.evaluate() == "Three of a kind")

    hand = PokerHand(
        TestDeck(
            [
                Card(9, "Hearts"),
                Card(9, "Clubs"),
                Card(5, "Diamonds"),
                Card(8, "Spades"),
                Card(5, "Hearts"),
            ]
        )
    )
    print(hand.evaluate() == "Two pair")

    hand = PokerHand(
        TestDeck(
            [
                Card(2, "Hearts"),
                Card(9, "Clubs"),
                Card(5, "Diamonds"),
                Card(9, "Spades"),
                Card(3, "Diamonds"),
            ]
        )
    )
    print(hand.evaluate() == "Pair")

    hand = PokerHand(
        TestDeck(
            [
                Card(2, "Hearts"),
                Card("King", "Clubs"),
                Card(5, "Diamonds"),
                Card(9, "Spades"),
                Card(3, "Diamonds"),
            ]
        )
    )
    print(hand.evaluate() == "High card")
