from random import shuffle

SUITS = ["heart", "diamond", "club", "spade"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
WINNING_POINT = 21


def prompt(msg):
    print(f"==> {msg}")


def calculate_hand(cards):
    total = 0
    num_of_aces = 0
    for card in cards:
        value = card[1]
        if value in ["J", "K", "Q"]:
            total += 10
        elif value == "A":
            total += 11
            num_of_aces += 1
        else:
            total += int(value)
    for _ in range(num_of_aces):
        if total > WINNING_POINT:
            total -= 10
    return total


def display_hand(cards, hide_rest=False):
    if hide_rest:
        print("Dealer Hands: " + f"({cards[0][1]} of {cards[0][0]})")
        return
    print("Player Hands: " + " ".join(
        [f"({value} of {suit})" for suit, value in cards]
    ))


def busted(hand):
    return calculate_hand(hand) > WINNING_POINT


def initialize_deck():
    deck = []
    for suit in SUITS:
        for value in VALUES:
            deck.append((suit, value))
    shuffle(deck)
    return deck


def deal(deck, hand):
    hand.append(deck.pop(0))


def game():
    def play():
        deck = initialize_deck()
        player_hand = []
        dealer_hand = []
        deal(deck, player_hand)
        deal(deck, player_hand)
        deal(deck, dealer_hand)
        deal(deck, dealer_hand)

        display_hand(player_hand)
        display_hand(dealer_hand, hide_rest=True)

        while True:
            prompt("hit or stay?")
            user_answer = input()

            if (user_answer == "stay" or busted(player_hand) or
                    calculate_hand(dealer_hand) == WINNING_POINT):
                break
            deal(deck, player_hand)

            if (busted(player_hand) or
                    calculate_hand(dealer_hand) == WINNING_POINT):
                break
            display_hand(player_hand)
        player_score = calculate_hand(player_hand)
        if busted(player_hand):
            prompt(f"Player total was {player_score}. Player losses!")
            return
        if player_score == WINNING_POINT:
            prompt("Player scores 21. Player wins!")
            return

        while calculate_hand(dealer_hand) < 17:
            deal(deck, dealer_hand)
        dealer_score = calculate_hand(dealer_hand)

        if busted(dealer_hand):
            prompt(f"Dealer total was {dealer_score}. You won!")
            return
        if dealer_score == WINNING_POINT:
            prompt(f"Dealer total was {dealer_score}. Dealer won!")
            return

        if dealer_score > player_score:
            prompt(f"Dealer total was {dealer_score}. \
            Player total was {player_score}. Dealer wins!")
        elif player_score > dealer_score:
            prompt(f"Dealer total was {dealer_score}. \
             Player total was {player_score}. Player wins!")
        else:
            prompt(f"Dealer total was {dealer_score}. \
            Player total was {player_score}. It's a tie!")

    prompt("Welcome to twenty-one!")
    while True:
        play()
        prompt("Do you want to play again? (y/n)")
        answer = input()
        if not (answer in ["y", "Y"]):
            break
    prompt("Thank you for playing!")


game()
