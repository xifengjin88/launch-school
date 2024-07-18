import random
import os


def prompt(msg):
    print(f"=> {msg}")


def display_board(board):
    os.system("clear")
    print("\n".join([" ".join(board[i:i + 3]) for i in range(0, 9, 3)]))


def is_winner(piece, winning_moves, board):
    return any([all([board[int(winning_move) - 1] == piece for winning_move in row]) for row in winning_moves])


def display_available_moves(board):
    return "".join(board) if len(board) <= 1 else ", ".join(board[:-1]) + " and " + board[-1]


def compute_available_moves(board, computer_piece, user_piece):
    return [move for move in board if move != user_piece and move != computer_piece]


def game():
    user_piece = "x"
    computer_piece = "o"

    def play():
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        winning_moves = [
            ["1", "2", "3", ],
            ["4", "5", "6", ],
            ["7", "8", "9", ],
            ["1", "4", "7"],
            ["2", "5", "8"],
            ["3", "6", "9"],
            ["1", "5", "9"],
            ["3", "5", "7"]
        ]

        while True:
            available_moves = compute_available_moves(board, computer_piece, user_piece)

            prompt(f"Please pick: {display_available_moves(available_moves)}")
            user_move = input()
            while user_move not in available_moves:
                prompt("Your selection is invalid.")
                prompt(f"Please pick: {display_available_moves(available_moves)}")
                user_move = input()

            board[int(user_move) - 1] = user_piece
            prompt(f"Player picked: {user_move}")
            display_board(board)
            print()
            available_moves = compute_available_moves(board, computer_piece, user_piece)
            if is_winner(user_piece, winning_moves, board):
                prompt("Player won!")
                break
            if not available_moves:
                prompt("It's a tie!")
                break
            computer_move = random.choice(available_moves)
            board[int(computer_move) - 1] = computer_piece
            prompt(f"Computer picked: {computer_move}")
            display_board(board)
            print()
            available_moves = compute_available_moves(board, computer_piece, user_piece)
            if is_winner(computer_piece, winning_moves, board):
                prompt("Computer won!")
                break

            if not available_moves:
                prompt("It's a tie!")
                break

    prompt("Welcome to tic tac toe!")

    while True:
        play()
        play_again = input("Would you like to play again? (y|n)")
        if play_again in ["n", "N"]:
            break
    prompt("Thanks for playing!")


game()
