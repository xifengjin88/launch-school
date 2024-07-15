import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"


def is_winner(move_a, move_b):
    return (move_a == ROCK and move_b == SCISSORS) or (move_a == PAPER and move_b == ROCK) or (move_a == SCISSORS and move_b == PAPER)


def valid_choice(choice):
    return choice in ["1", "2", "3"]


def prompt(message):
    print(f"==> {message}")


def computer_choice():
    choice = random.randint(0, 2)
    return [ROCK, PAPER, SCISSORS][choice]


def play():
    prompt("Player make a move. \n1) Rock 2) Paper 3) Scissors")
    moves = [ROCK, PAPER, SCISSORS]
    player_choice = input()

    while not valid_choice(player_choice):
        prompt("Enter a valid option")
        player_choice = input()
    player_move = moves[int(player_choice) - 1]
    computer_move = computer_choice()
    prompt(f"Computer picked {computer_move}")
    if is_winner(player_move, computer_move):
        prompt("Player won!")
    elif is_winner(computer_move, player_move):
        prompt("Computer won!")
    else:
        prompt("It's a draw!")


def main():
    prompt("Welcome to Rock Paper and Scissors game!")
    while True:
        play()
        prompt("Would you like to play again? (y|n) ")
        play_again = input()
        if play_again and play_again.strip().lower() != "y":
            break


main()
