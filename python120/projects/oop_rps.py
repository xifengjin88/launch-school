from random import choice

def prompt(msg):
    print(f"==> {msg}")


class Move:
    ROCK = 'r'
    PAPER = 'p'
    SCISSORS = 's'
    VALID_MOVES = [ROCK, PAPER, SCISSORS]

    def __init__(self, move):
        self._move = move

    def __str__(self):
        return self.move

    @property
    def move(self):
        return self._move

    def __eq__(self, other):
        return self.move == other.move


class Player:
    def __init__(self, name=None):
        if not name:
            prompt("What is your name: ")
            name = input().strip()
        self._name = name

    def choose(self):
        prompt("Please choose rock, paper or scissors? \
         (rock -> r, paper -> p, scissors -> s")
        answer = input().strip().lower()
        while True:
            if answer in Move.VALID_MOVES:
                break
            prompt("Your answer was not valid, please try again.")
        return Move(answer)


class Computer(Player):
    def choose(self):
        return Move(choice(Move.VALID_MOVES))


class Rule:

    def __init__(self):

        self._winning = [
            [Move(Move.ROCK), Move(Move.SCISSORS)],
            [Move(Move.PAPER), Move(Move.ROCK)],
            [Move(Move.SCISSORS), Move(Move.PAPER)]
        ]

    def compare(self, move1, move2):
        if move1 == move2:
            return 'tie'
        for winning_move in self._winning:
            if move1 == winning_move[0] and move2 == winning_move[1]:
                return 'win'
        return 'lose'


class RPSGame:
    def __init__(self):
        self._player = Player()
        self._computer = Computer("computer")
        self._rule = Rule()
        self._player_move = None
        self._computer_move = None

    def display_welcome_message(self):
        prompt("Welcome to RPS Game!")

    def display_goodbye_message(self):
        prompt("Goodbye!")

    def display_winner(self):
        result = self._rule.compare(self._player_move, self._computer_move)
        if result == 'tie':
            prompt("it's a tie!")
        elif result == 'win':
            prompt("You won!")
        else:
            prompt("You lost!")

    def play(self):
        self.display_welcome_message()
        self.player_choose()
        self.computer_choose()
        self.display_winner()
        self.display_goodbye_message()

    def player_choose(self):
        self._player_move = self._player.choose()

    def computer_choose(self):
        self._computer_move = self._computer.choose()
        prompt(f"Computer picked: {self._computer_move}")


if __name__ == '__main__':
    game = RPSGame()
    game.play()
