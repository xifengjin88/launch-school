import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
LIZARD = 'lizard'
SPOCK = 'spock'

CHOICES = {
    "r": ROCK,
    "p": PAPER,
    "s": SCISSORS,
    "sp": SPOCK,
    "l": LIZARD
}
VALID_CHOICES = list(CHOICES.keys())
WINNING_SCORE = 3


def prompt(message):
    print(f"==> {message}")


def is_winner(player_1, player_2):
    return (player_1 == ROCK and player_2 == SCISSORS) or \
        (player_1 == PAPER and player_2 == ROCK) or \
        (player_1 == SCISSORS and player_2 == PAPER) or \
        (player_1 == SPOCK and player_2 == SCISSORS) or \
        (player_1 == LIZARD and player_2 == PAPER) or \
        (player_1 == PAPER and player_2 == SPOCK) or \
        (player_1 == ROCK and player_2 == LIZARD) or \
        (player_1 == LIZARD and player_2 == SPOCK) or \
        (player_1 == SPOCK and player_2 == SCISSORS) or \
        (player_1 == SCISSORS and player_2 == LIZARD) or \
        (player_1 == SPOCK and player_2 == ROCK)


def computer_make_choice():
    return random.choice(list(CHOICES.values()))


def player_make_choice():
    prompt("""Player make a move.
    r) Rock p) Paper s) Scissors sp) Spock l) Lizard """)
    choice = input()
    while not choice in VALID_CHOICES:
        prompt(f"Please enter {", ".join(VALID_CHOICES)}.")
        choice = input()
    return CHOICES[choice]


def announce_winner(player_score, computer_score):
    if player_score > computer_score:
        prompt(f"Player won the game! score {
               player_score} vs {computer_score}")
    elif computer_score > player_score:
        prompt(f"Computer won the game! score {
               player_score} vs {computer_score}")
    else:
        prompt("It's a tie!")


def play_game():
    player_score = 0
    computer_score = 0
    while True:
        player_choice = player_make_choice()
        computer_choice = computer_make_choice()
        if is_winner(player_1=player_choice, player_2=computer_choice):
            player_score += 1
            prompt(f"""You picked {player_choice} and Computer picked {
                   computer_choice}. You won this round!""")
        elif is_winner(player_1=computer_choice, player_2=player_choice):
            computer_score += 1
            prompt(f"You picked {player_choice} and Computer picked {
                   computer_choice}. Computer won!")
        else:
            prompt(f"You picked {player_choice} and Computer picked {
                   computer_choice}. It's a tie!")
        if computer_score >= WINNING_SCORE or player_score >= WINNING_SCORE:
            announce_winner(player_score, computer_score)
            break


def main():
    prompt(f"Welcome to the game {", ".join(list(CHOICES.values()))}")
    while True:
        play_game()
        prompt("Would you like to play again? (y|n) ")
        response = input()
        while not (response and (response.startswith("y") or
                                 response.startswith("n"))):
            prompt("Please enter y or n.")
            response = input()
        if response == "n":
            break


main()
