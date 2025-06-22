from random import choice

EMPTY_PIECE = " "
COMPUTER_PIECE = "O"
HUMAN_PIECE = "X"


class Board:
    WINNING_MOVES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    def __init__(self):
        self.board = {
            "1": " ",
            "2": " ",
            "3": " ",
            "4": " ",
            "5": " ",
            "6": " ",
            "7": " ",
            "8": " ",
            "9": " "
        }

    def display(self):
        print("     |     |     ")
        print(f"  {self.board["1"]}  |  {self.board["2"]}  |  {self.board["3"]}  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.board["4"]}  |  {self.board["5"]}  |  {self.board["6"]}  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.board["7"]}  |  {self.board["8"]}  |  {self.board["9"]}  ")
        print("     |     |     ")

    def update(self, position, piece):
        self.board[position] = piece

    @property
    def valid_moves(self):
        return [position for position, piece in self.board.items() if piece == EMPTY_PIECE]

    def has_winning_moves(self, piece):
        return any([all([piece == self.board[str(move)] for move in moves]) for moves in Board.WINNING_MOVES])

    @property
    def is_full(self):
        return len(self.valid_moves) == 0


class Player:

    def move(self, board, position, piece):
        board.update(position, piece)


class Human(Player):
    def move(self, board):
        position = input("Player, please pick a move: ")
        while position not in board.valid_moves:
            print("please enter a valid move")
            position = input("Please pick a move: ")
        super().move(board, position, HUMAN_PIECE)


class Computer(Player):

    def move(self, board):
        position = choice(board.valid_moves)
        super().move(board, position, COMPUTER_PIECE)


class Game:
    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.board = Board()

    def has_player_won(self):
        return self.board.has_winning_moves(HUMAN_PIECE)

    def has_computer_won(self):
        return self.board.has_winning_moves(COMPUTER_PIECE)

    def has_winner(self):
        return self.has_player_won() or self.has_computer_won()


    def reset_board(self):
        self.board = Board()

    def play(self):
        self.welcome_message()
        self.board.display()
        while True:
            self.human.move(self.board)
            if self.has_winner():
                break
            self.computer.move(self.board)
            if self.has_winner():
                break
            self.board.display()
        self.board.display()
        if self.has_winner():

            if self.has_computer_won():
                self.prompt("Computer has won!")
            elif self.has_player_won():
                self.prompt("You won! Congrats!")
        else:
            self.prompt("It's a tie!")
        if self.play_again():
            self.reset_board()
            self.play()
        else:
            self.display_goodbye_message()

    def prompt(self, msg):
        print(f"==> {msg}")

    def welcome_message(self):
        self.prompt("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        self.prompt("Bye! Hope to see you again")

    def play_again(self):
        answer = input("Would you like to play again? (y/n): ")
        while answer not in ["y", "Y", "n", "N"]:
            self.prompt("Please enter either 'y' or 'n'.")
            answer = input("Would you like to play again? (y/n): ")
        return answer in ["y", "Y"]


if __name__ == "__main__":
    ttt = Game()
    ttt.play()
