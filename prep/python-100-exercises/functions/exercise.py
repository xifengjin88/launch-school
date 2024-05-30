# Examine the function invocation below. Write the function multiply, such that it accepts two arguments and returns the product of its arguments. You may assume that the function arguments will always be numbers.

def multiply(a, b):
  return a * b

# Write a function that prints Bruce Eckel's quote 'Python is executable pseudocode.'. What is the return value of the function?

def bruce_eckel_quote():
  print('Python is executable pseudocode.')

# Let's generalize the function from the previous exercise. Implement a function named cite that takes two string arguments: the author of the quote and what they said. It then prints the quote, as shown below.

def cite(author, quote):
  print(f'{author} said: "{quote}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')

# Write a function that accepts a single argument, a number, and returns the result of multiplying its argument by an exponent of 2 (also known as squaring the number or raising the number to the power of 2).

def squared_number(n):
  return n ** 2


# Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length. For example:

def compare_by_length(a, b):
  len_a = len(a)
  len_b = len(b)
  if len_a == len_b:
    return 0
  elif len_a < len_b:
    return -1
  else:
    return 1


print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0

# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

s = "Captain Ruby"

s = s.replace("Ruby", "Python")

# Use Python's control structures to create a function that takes an ISO 639-1 language code and returns a greeting in that language. You can take the examples below or add whatever languages you like.

def greet(lang_code):
  match lang_code:
    case "en":
      return "Hi!"
    case "fr":
      return "Salut!"
    case "pt":
      return "Olá!"
    case "de":
      return "Hallo!"
    case "sv":
      return "Hej!"
    case "af":
      return "Haai!"
    case _:
      return "unknown code"



print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!

# Write a function that extracts the language code from a locale. A locale is a combination of a language code, a region, and usually also a character set, e.g en_US.UTF-8.

def extract_language(code):
  return code.split(".")[0].split("_")[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

# Similar to the previous exercise, write a function that extracts the region code from a locale. For example:

def extract_region(s):
   return s.split(".")[0].split("_")[1]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

# Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when they share a common language, for example:

def local_greet(s):
  language = extract_language(s)
  region = extract_region(s)
  if language == "en":
    match region:
      case "US":
        return "Hey!"
      case "GB":
        return "Hello!"
      case "AU":
        return "Howdy!"
  else:
    return "Salut!"


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!




