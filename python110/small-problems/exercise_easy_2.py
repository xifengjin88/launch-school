from math import floor, ceil

DEGREE = "\u00B0"


def format_degree(degree, minutes, sec):
    return f"{degree}{DEGREE}{minutes:02}'{sec:02}\""


def dms(angle):
    if angle == 0:
        return format_degree(0, 0, 0)
    elif angle < 0:
        return dms(angle + 360)
    elif angle > 360:
        return dms(angle % 360)
    else:
        degree = floor(angle)
        minutes = floor((angle - degree) * 60)
        sec = floor(((angle - degree) * 60 - minutes) * 60)
        return format_degree(degree, minutes, sec)


def union(lst1, lst2):
    return set(lst1) | set(lst2)


def halvsies(lst):
    mid = ceil(len(lst) / 2)
    return [lst[:mid], lst[mid:]]


def find_dup(lst):
    d = {}
    for item in lst:
        d[item] = d.get(item, 0) + 1
        if d[item] > 1:
            return item


def interleave(lst1, lst2):
    result = []
    for l in zip(lst1, lst2):
        result.extend(list(l))
    return result


def multiplicative_average(lst):
    total = 1
    for item in lst:
        total *= item
    return f"{total / len(lst):.3f}"


def multiply_list(lst1, lst2):
    return [item[0] * item[1] for item in zip(lst1, lst2)]


def digit_list(nums):
    result = []
    while nums:
        result.insert(0, nums % 10)
        nums = nums // 10
    return result


def count_occurrences(car_list):
    result = {}
    for car in car_list:
        result[car] = result.get(car, 0) + 1

    for car_name, count in result.items():
        print(f"{car_name} => {count}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

VOWELS = 'aeiou'


def average(nums):
    return floor(sum(nums) / len(nums))


def repeater(s):
    return "".join([char * 2 for char in s])


def double_consonants(s):
    return "".join([char * 2 if not (char in VOWELS) and char.isalpha() else char for char in s])


def sequence(count, initial_value):
    result = []
    for i in range(count):
        result.append(initial_value * (i + 1))

    return result

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

def is_balanced(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0
