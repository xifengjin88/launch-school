import sys

sys.set_int_max_str_digits(50_000)


def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    if len(lst) == 0:
        return []
    return lst[1:] + [lst[0]]


# def rotate_rightmost_digits(digit, count):
#     count = count % (len(str(digit)) + 1)
#     tens_place = 10 ** count
#     before, after = digit // tens_place, digit % tens_place
#     before = before * tens_place
#     digits_to_put_back, digit_to_rotate = after % (10 ** (count - 1)), after // (10 ** (count - 1))
#
#     return before + digits_to_put_back * 10 + digit_to_rotate


def rotate_string(s):
    return s[1:] + s[0]


def rotate_rightmost_digits(digit, count):
    str_digit = str(digit)
    front = str_digit[:-count]
    end = str_digit[-count:]
    return int(front + rotate_string(end))


def max_rotation(digit):
    for n in range(len(str(digit)), 1, -1):
        digit = rotate_rightmost_digits(digit, n)
    return digit


def word_to_digit(msg):
    words = [
        ("zero", "0"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]

    for word, number in words:
        msg = msg.replace(word, number)
    return msg


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


import math


def is_prime_solution(number):
    if number == 1:
        return False

    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True


def fibonacci(n):
    a, b = 1, 1
    if n <= 2:
        return 1
    i = 3
    while i <= n:
        a, b = b, a + b
        i += 1
    return b


def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


#
# print(fibonacci_recursive(1) == 1)         # True
# print(fibonacci_recursive(2) == 1)         # True
# print(fibonacci_recursive(3) == 2)         # True
# print(fibonacci_recursive(4) == 3)         # True
# print(fibonacci_recursive(5) == 5)         # True
# print(fibonacci_recursive(6) == 8)         # True
# print(fibonacci_recursive(12) == 144)      # True
# print(fibonacci_recursive(20) == 6765)     # True

def fibonacci_memo(n, cache={}):
    if n <= 2:
        return 1
    if n in cache:
        return cache[n]
    cache[n - 1] = fibonacci_memo(n - 1, cache)
    cache[n - 2] = fibonacci_memo(n - 2, cache)
    return cache[n - 1] + cache[n - 2]


def find_fibonacci_index_by_length(num_digits):
    n = 1
    cache = {}

    while True:
        fib_value = fibonacci_memo(n, cache)
        if len(str(fib_value)) == num_digits:
            return n
        n += 1
