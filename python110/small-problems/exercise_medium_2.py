from datetime import datetime


def letter_percentages(s):
    upper_count = 0
    lower_count = 0
    neither_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        else:
            neither_count += 1
    total_count = len(s)
    return {
        "uppercase": f"{(upper_count / total_count) * 100:.2f}",
        "lowercase": f"{(lower_count / total_count) * 100:.2f}",
        "neither": f"{(neither_count / total_count) * 100:.2f}"
    }


# def is_valid_triangle(a, b, c):
#     if 0 in [a, b, c]:
#         return False
#     a, b, c = sorted([a, b, c])
#     return a + b > c


# def triangle(a, b, c):
#     group = {a, b, c}
#     if not is_valid_triangle(a, b, c):
#         return "invalid"
#
#     if len(group) == 1:
#         return "equilateral"
#     elif len(group) == 2:
#         return "isosceles"
#     else:
#         return "scalene"


def friday_the_13ths(year):
    weekday = 4
    date = 13
    count = 0
    for month in range(1, 13):
        if datetime(year, month, date).weekday() == weekday:
            count += 1
    return count


def has_dup(n):
    seen = set()
    print(n)
    for i in str(n):

        if i in seen:
            return True
        seen.add(i)
    return False


def is_featured(n):
    return n % 7 == 0 and n % 2 == 1 and not has_dup(n)


def next_featured(n):
    n += 1
    max_value = 9876543201
    if n > max_value:
        return "There is no possible number that fulfills those requirements."
    while n < max_value:
        if is_featured(n):
            return n
        n += 1
    return max_value


def sum_square_difference(n):
    square_sum = sum([i for i in range(1, n + 1)]) ** 2
    sum_of_squares = sum([i ** 2 for i in range(1, n + 1)])
    return square_sum - sum_of_squares


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                swap(lst, i, j)
    return lst




def is_valid_triangle(a, b, c):
    return sum([a, b, c]) == 180 and a > 0 and b > 0 and c > 0


def triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "invalid"
    if 90 in [a, b, c]:
        return "right"
    if a < 90 and b < 90 and c < 90:
        return "acute"
    if len([angle for angle in [a, b, c] if angle > 90]) == 1:
        return "obtuse"
