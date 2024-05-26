'''
Write a program named age.py that asks the user to enter their age, 
then calculates and reports the future age 10, 20, 30, and 40 years from now. 
Here's the output for someone who is 27 years old.
'''

# age = int(input("How old are you? "))

# print(f"You are {age} years old.")

# for i in range(4):
#   increment = 10
#   year = (i + 1) * increment
#   age += increment
#   print(f"In {year} years, you will be {age}")


# my_list = [6, 3, 0, 11, 20, 4, 17]

# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1

# for item in my_list:
#   print(item)


# i = 0
# while i < len(my_list):
#   number = my_list[i]
#   if number % 2 == 0:
#     print(number)
#   i += 1

# print("-------------------------------")
# for number in my_list:
#   if number % 2 != 0:
#     print(number)

  
# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for inner_list in my_list:
#   for number in inner_list:
#     if number % 2 == 0:
#       print(number)

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# def process(number):
#   return "odd" if number % 2 != 0 else "even"

# my_list = [process(number) for number in my_list]

# print(my_list)

# def find_integers(t):
#   return [item for item in t if type(item) is int]

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# integers = find_integers(my_tuple)
# print(integers)

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# def factorial_recursive(n):
#   return n * factorial_recursive(n - 1)

# def factorial_iter(n):
#   result = 1
#   while n > 0:
#     result *= n
#     n -= 1
#   return result

# print(factorial_iter(1))   # 1
# print(factorial_iter(2))   # 2
# print(factorial_iter(3))   # 6
# print(factorial_iter(4))   # 24
# print(factorial_iter(5))   # 120
# print(factorial_iter(6))   # 720
# print(factorial_iter(7))   # 5040
# print(factorial_iter(8))   # 40320
# print(factorial_iter(25))  # 15511210043330985984000000

# import random

# highest = 10

# while True:

#     number = random.randrange(highest + 1)
#     print(number)
#     if highest == number:
#         break
 
   
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]


[print(item) 
  for nest_list in my_list
  for item in nest_list if item % 2 == 0
]
