import json

with open("calculator_messages.json", "r") as file:
    data = json.load(file)


message = data["zh"]


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


def game():
    prompt(message["first_number"])
    number1 = input()
    while not valid_number(number1):
        prompt(message["number_validation"])
        number1 = input()

    prompt(message["second_number"])
    number2 = input()
    while not valid_number(number2):
        prompt(message["number_validation"])
        number2 = input()

    prompt(message["operation"])
# rest of the code omitted
    operation = input()
    while not valid_operation(operation):
        prompt(message["operation_validation"])
        operation = input()

    result = calculate(float(number1), float(number2), operation)
    prompt(f"Result is {result}")


def main():
    prompt(message["greeting"])

    while True:
        game()
        prompt(message["play_again"])
        response = input()
        if response != "y":
            break


main()
