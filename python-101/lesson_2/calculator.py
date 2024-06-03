
def is_digit(n):
    return n.isnumeric()

def is_operator(c):
    return c in ["*", "/", "+", "-"]


def validate(n, predicate, error_message, prompt):
    while not predicate(n):
        print(error_message)
        n = input(prompt)
    return n

def calculate(n, m, operator):
    match operator:
        case "+":
            return n + m
        case "-":
            return n - m
        case "/":
            return n / m
        case "*":
            return n * m
    


def main():
    num1 = input("Enter number 1: ")
    num1 = validate(num1, is_digit, f"Value {num1} is not valid, please enter a number", "Enter number 1: ")
    num2 = input("Enter number 2: ")
    num2 = validate(num2, is_digit, f"Value {num2} is not valid, please enter a number", "Enter number 2: ")
    operator = input("Enter an operator: ")
    operator = validate(operator, is_operator, f"Operator {operator} is not valid, please enter a  valid operator. ", "Enter an operator: ")
    result = calculate(int(num1), int(num2), operator)
    print(f"{num1} {operator} {num2} = {result}")
  


main()