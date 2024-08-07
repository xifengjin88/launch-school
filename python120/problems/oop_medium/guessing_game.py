from random import randint


class GuessingGame:
    def __init__(self):
        self._guesses_left = 7
        self._random_number = randint(1, 100)

    @staticmethod
    def validate(guess):
        return 0 <= guess <= 100

    def play(self):
        while True:
            if self._guesses_left == 0:
                print("You have no more guesses. You lost!")
                break

            print(f"You have {self._guesses_left} guesses remaining.")
            print("Enter a number between 1 - 100: ")
            guess = int(input().strip())
            while not GuessingGame.validate(guess):
                print("Invalid guess. Enter a number between 1 and 100:")
                guess = int(input().strip())
            if guess == self._random_number:
                print("That's the number!")
                print()
                print("You won!")
                break
            elif guess > self._random_number:
                print("Your guess is too high")
            else:
                print("Your guess is too low")

            self._guesses_left -= 1


if __name__ == "__main__":
    game = GuessingGame()
    game.play()
