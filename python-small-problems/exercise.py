# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# def is_odd(num):
#   return abs(num) % 2 == 1


# print(is_odd(1) == True)
# print(is_odd(-3) == True)
# print(is_odd(2) == False)
# print(is_odd(-2) == False)

# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# for i in range(1, 100):
#   if is_odd(i):
#     print(i)

# for i in range(1, 100, 2):
#   print(i)

# for i in range(1, 100):
#   if not is_odd(i):
#     print(i)

# for i in range(2, 100, 2):
#   print(i)

# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# length = int(input("Enter the length of the room in meters: "))
# width = int(input("Enter the width of the room in meters: "))

# area = length * width
# square_feet_in_meter = 10.7639

# print(f"The area of the room in meters is {area} square meters.")

# print(f"The area of the room in sq is {area * square_feet_in_meter:.2f} square feet.")

# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

# def tip_calculator():
#   bill = float(input("What is the bill? "))
#   tip_percentage = float(input("What is the tip percentage? "))
  
#   tip = tip_percentage * 0.01 * bill
#   total = bill + tip
#   print(f"The tip is ${tip:.2f}")
#   print(f"The total is ${total:.2f}")


# tip_calculator()


# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# def compute_sum(n):
#   total = 0
#   for i in range(1, n + 1):
#     total += i
#   return total

# def compute_product(n):
#   product = 1
#   for i in range(1, n + 1):
#     product *= i
#   return product

# number = int(input("Please enter an integer greater than 0: "))

# command = input('Enter "s" to compute the sum, or "p" to compute the product. ')

# if command == 's':
#   result = compute_sum(number)
#   print(f"The sum of the integers between 1 and {number} is {result}.")
# elif command == 'p':
#   result = compute_product(number)
#   print(f"The product of the integers between 1 and {number} is {result}.")


# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

def short_long_short(s1, s2):
  if len(s1) < len(s2):
    return s1 + s2 + s1
  return s2 + s1 + s2


# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# leap year 1

def is_leap_yearv1(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False
  
def is_leap_year(year):
  if year < 1752:
    return year % 4 == 0
  return is_leap_yearv1(year)
  
# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.


def multisum(n):
  def predicate(n):
    return n % 3 == 0 or n % 5 == 0
  s = 0
  for i in range(1, n + 1):
    if predicate(i):
      s += i
  return s


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

def utf16_value(s):
  return sum([ord(char) for char in s])
  


# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)