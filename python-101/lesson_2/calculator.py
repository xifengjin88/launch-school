def prompt(msg):
    print(f"==> {msg}")


def valid_number(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def valid_operation(o):
    return o in ['1', '2', '3', '4']


def calculate(num1, num2, operation):
    match operation:
        case "1":
            return num1 + num2
        case "2":
            return num1 - num2
        case "3":
            return num1 * num2
        case "4":
            return num1 / num2


def main():
    prompt("Welcome to calculator!")
    prompt("What is your first number? ")
    number1 = input()
    while not valid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What is your second number? ")
    number2 = input()
    while not valid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    prompt("What operation would you like to perform?")
    prompt("1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()
    while not valid_operation(operation):
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    result = calculate(int(number1), int(number2), operation)
    prompt(f"Result is {result}")


main()
