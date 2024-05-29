# def do_something(dictionary):
#     return sorted(dictionary.keys())[1].upper()

# my_dict = {
#     'Karl':     108,
#     'Clare':    175,
#     'Karis':    140,
#     'Trevor':   180,
#     'Antonina': 132,
#     'Chris':    101,
# }

# print(do_something(my_dict)) # CHRIS

# from math import sqrt

# print(sqrt(37))

# def square(num):
#     return num * num

# def sum_of_squares(num1, num2):
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

counter = 0

# def increment_counter():
#   global counter
#   counter += 1

# print(counter)                # 0

# increment_counter()
# print(counter)                # 1

# increment_counter()
# print(counter)                # 2

# counter = 100
# increment_counter()
# print(counter)                # 101

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

