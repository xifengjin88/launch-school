# Write a program that solicits six (6) numbers from the user and
# prints a message that describes whether the sixth number appears
# among the first five.
#
from typing import List


# numbers = []
# times = ["1st", "2nd", "3rd", "4th", "5th", "last"]
# last_number = None
#
# for time in times:
#     number = int(input(f"Enter the {time} number: "))
#     if len(numbers) < len(times) - 1:
#         numbers.append(number)
#     last_number = number
#
# msg = "is" if last_number in numbers else "isn't"
# numbers_string = ",".join([str(num) for num in numbers])


# Write a function that returns True if the string passed as an argument
# is a palindrome, False otherwise. A palindrome reads the same forwards
# and backwards. For this problem, the case matters and all characters matter.

def is_palindrome(s: str) -> bool:
    return s == s[::-1]


# Write another function that returns True if the
# string passed as an argument is a palindrome, or
# False otherwise. This time, however, your function should be
# case-insensitive, and should ignore all non-alphanumeric characters.
# If you wish, you may simplify things by calling the is_palindrome function
# you wrote in the previous exercise.

def is_real_palindrome(s: str) -> bool:
    s = "".join([char for char in s if s.isalnum()]).lower()
    return is_palindrome(s)


# Write a function that takes a list of numbers and returns a
# list with the same number of elements, but with each element's
# value being the running total from the original list.
#

def running_total(nums: List[int]) -> List[int]:
    total = 0
    new_nums = []
    for num in nums:
        new_nums.append(num + total)
        total += num
    return new_nums


# Write a function that takes a string consisting of
# zero or more space-separated words and returns a dictionary
# that shows the number of words of different sizes.
# Words consist of any sequence of non-space characters.
#


# def word_sizes(s: str) -> dict[int, int]:
#     result = {}
#     for word in s.split():
#         result[len(word)] = result.get(len(word), 0) + 1
#
#     return result


def word_sizes(s: str) -> dict[int, int]:
    result = {}
    for word in s.split():
        new_word = "".join([char for char in list(word) if char.isalnum()])
        if len(new_word) > 0:
            result[len(new_word)] = result.get(len(new_word), 0) + 1

    return result


# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})
#
# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})
#
# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})
#
# string = "What's up ???"
# print(word_sizes(string) == {5: 1, 2: 1})
#
# print(word_sizes('') == {})

#
#
# Given a string of words separated by spaces, write a function
# that swaps the first and last letters of every word.
#
# You may assume that every word contains at least one letter,
# and that the string will always contain at least one word.
# You may also assume that each string contains nothing but words
# and spaces, and that there are no leading, trailing, or repeated spaces.

def swap(s: str) -> str:
    return " ".join([word[-1] + word[1:-1] + word[0] if len(word) > 1 else word for word in s.split()])


# Write a function that takes a string of digits and
# returns the appropriate number as an integer.
# You may not use any of the standard conversion
# functions available in Python, such as int.
# Your function should calculate the result by using the characters in the string.
#
# For now, do not worry about leading + or - signs,
# nor should you worry about invalid characters;
# assume all characters are numeric.

def string_to_integer(s: str) -> int:
    result = 0
    for char in s:
        result = result * 10 + int(char)
    return result


def string_to_signed_integer(s):
    digits = {}
    for i in range(10):
        digits[str(i)] = i
    sign = None
    result = 0
    for char in s:
        if not (char in digits):
            sign = char
        else:
            result = result * 10 + digits[char]
    return result if sign is None or sign == "+" else -result

def integer_to_string(num):
    result = ""
    digits = {}
    for i in range(10):
        digits[i] = str(i)

    while True:
        result = digits[num % 10] + result
        num //= 10
        if num == 0:
            break
    return result


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True