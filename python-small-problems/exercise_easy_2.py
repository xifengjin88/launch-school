# Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.

def greetings(name, info):
    full_name = " ".join(name)
    title = f"{info["title"]} {info["occupation"]}"
    return f"Hello, {full_name}! Nice to have a {title} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

def greet_a_user():
    name = input("What is your name? ")
    if len(name) > 0:
        if name.endswith("!"):
            print(f"HELLO {name.upper()}! WHY ARE WE YELLING?")
        else:
            print(f"Hello {name}.")


# Create a function that takes two arguments, multiplies them together, and returns the result.

def multiply(a, b):
    return a * b

# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).


def square(n):
    return multiply(n, n)



# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

def calculate(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "//":
            return num1 // num2
        case "%":
            return num1 % num2
        case "**":
            return num1 ** num2
        


def calculator():
    operators = ["+", "-", "*", "/", "//", "%", "**"]
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    for operator in operators:
       result = calculate(num1, num2, operator)
       print(f"{num1} {operator} {num2} = {result}")
    


# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.
    
def penultimate(sentence):
    return sentence.split()[-2]

# The or operator returns a truthy value if either or both of its operands are truthy, a falsy value if both operands are falsy. The and operator returns a truthy value if both of its operands are truthy, and a falsy value if either operand is falsy. This works great until you need only one of two conditions to be truthy, the so-called exclusive or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

def xor(a, b):
    return bool(a) != bool(b)

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.


def oddities(nums):
    return nums[::2]


# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

from random import randint

teddy_age = randint(20, 100)
# print(f"Teddy is {age} years old!")

# Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime

# age = int(input("What is your age? "))
# retirement_age = int(input("At what age would you like to retire? "))

# years_to_go = retirement_age - age
# current_year = datetime.today().year

# print(f"It's {current_year}. You will retire in {current_year + years_to_go}")
# print(f"You have only {years_to_go} years of work to go!")

# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

def center_of(s):
    middle = len(s) // 2
    return s[middle] if len(s) % 2 == 1 else s[middle - 1:middle + 1]

# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")  

def negative(num):
    return -abs(num)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

