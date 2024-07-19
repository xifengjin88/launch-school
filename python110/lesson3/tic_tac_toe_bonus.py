
import random

USER_PIECE = "X"
COMPUTER_PIECE = "O"
INITIAL_MARK = " "

WINNING_LINES = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]


def prompt(msg):
    print(f"==> {msg}")


def display_board(board):

    print()
    print("     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |   {board[3]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |   {board[6]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |   {board[9]}  ")
    print("     |     |     ")


def initialize_board():
    return {key: INITIAL_MARK for key in range(1, 10)}


def board_full(board):
    return len([value for value in board.values() if value == INITIAL_MARK]) == 0


def detect_winner(piece, board):
    return any([all([board[winning_move] == piece for winning_move in winning_line]) for winning_line in WINNING_LINES])


def winner(board):
    if detect_winner(USER_PIECE, board):
        return USER_PIECE
    elif detect_winner(COMPUTER_PIECE, board):
        return COMPUTER_PIECE


def find_available_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARK]


def player_place_move(board):
    available_squares = find_available_squares(board)

    while True:
        prompt(f"Pick a piece: {join_or(available_squares)}")

        user_move = int(input())
        if user_move in available_squares:
            break
        prompt("Sorry, your pick was invalid")
    board[user_move] = USER_PIECE


def computer_place_move(board):
    available_squares = find_available_squares(board)
    computer_move = random.choice(available_squares)
    board[computer_move] = COMPUTER_PIECE


def join_or(lst, word_delimiter=", ", ending_delimiter="or"):
    str_list = [str(item) for item in lst]
    if len(str_list) <= 1:
        return "".join(str_list)
    elif len(str_list) <= 2:
        return " ".join([str_list[0]] + [ending_delimiter] + [str_list[-1]])
    return word_delimiter.join(str_list[:-1] + [ending_delimiter + " " + str_list[-1]])


def has_won(board):
    return bool(winner(board))


def game():
    prompt("Welcome to Tic Tac Toe!")

    user_score = 0
    computer_score = 0

    def play():
        board = initialize_board()

        display_board(board)
        while True:
            player_place_move(board)
            if has_won(board) or board_full(board):
                break
            computer_place_move(board)
            if has_won(board) or board_full(board):
                break
            display_board(board)
        display_board(board)
        if has_won(board):
            final_winner = winner(board)
            print("You won!") if final_winner == USER_PIECE else print("Computer Won!")
        else:
            print("It's a tie!")

    while True:
        play()
        prompt("Would you like to play again?")
        play_again = input()
        if play_again in ["n", "N"]:
            break
    prompt("Thank you for playing!")

game()