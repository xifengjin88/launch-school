# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.


def repeat(s, n):
    for _ in range(n):
        print(s)


# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.


def crunch(s):
    new_s = ""
    index = 0
    while index < len(s):
        if index == len(s) - 1 or s[index] != s[index + 1]:
            new_s += s[index]
        index += 1

    return new_s


# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# Write a function that takes a short line of text and prints it within a box.


def print_in_box(s):
    middle_width = len(s) + 2
    top = f"+{"-" * middle_width}+"
    bottom = f"+{"-" * middle_width}+"
    row = f"|{" " * middle_width}|"
    content = f"|{s.center(middle_width)}|"
    print(f"""
    {top}
    {row}
    {content}
    {row}
    {bottom}
    """)

# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.


def stringy(n):
    return "".join(["1" if n % 2 == 1 else "0" for n in range(1, n + 1)])


# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True


# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.
def triangle(n):
    return "\n".join([("*" * i).rjust(n) for i in range(1, n + 1)])


# A double number is an even-length number whose left-side digits are exactly the same as its right-side digits. For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

# Write a function that returns the number provided as an argument multiplied by two, unless the argument is a double number. If the argument is a double number, return the double number as-is.

def twice(n):
    def is_double(n):
        n_str = str(n)
        if len(n_str) % 2 == 1:
            return False
        half = len(n_str) // 2
        left = n_str[:half]
        right = n_str[half:]
        return left == right
    return n if is_double(n) else n * 2


# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True


# Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'
# Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.

def get_grade(a, b, c):
    score = (a + b + c) / 3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'not valid'


# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

# Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

def clean_up(s):
    new_str = ""
    for char in s:
        if not char.isalnum():
            if new_str and new_str[len(new_str) - 1] == " ":
                new_str += ""
            else:
                new_str += " "
        else:
            new_str += char
    return new_str


# print(clean_up("---what's my +*& line?") == " what s my line ")

# Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

def suffix(year):

    if year == 1:
        return 'st'
    elif year == 2:
        return "nd"
    elif year == 3:
        return "rd"
    elif year > 100:
        return suffix(year % 100)
    elif year > 20:
        return suffix(year % 10)
    else:
        return "th"


def century(year):
    c, r = year // 100, year % 100
    if r != 0:
        c += 1
    return f"{c}{suffix(c)}"


# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True

def matlib():
    print("Enter a noun: ")
    noun = input()
    print("Enter a verb: ")
    verb = input()
    print("Enter an adjective: ")
    adjective = input()
    print("Enter an adverb: ")
    adverb = input()
    print(f"""
    Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!
    The {adjective} {noun} {verb} {adverb} over the lazy {noun}.
    The {noun} {adverb} {verb} up to Joe's {adjective} turtle.
    """)


def mutating_delete(lst):
    if is_empty(lst):
        return lst
    lst.pop(-1)
    return lst


def is_empty(lst):
    return len(lst) == 0


def non_mutating_delete(lst):
    if is_empty(lst):
        return lst
    return lst[:-1]
    # your code goes here


# lst = [1, 2, 3]

# print(mutating_delete(lst) == [1, 2])  # => True
# print(lst == [1, 2])

bar = 0
foo = ['']
baz = 3
qux = (bar > baz) or bar and baz or foo

print(qux)

if qux:
    print("Operation succeeded")
else:
    print("Operation failed")
