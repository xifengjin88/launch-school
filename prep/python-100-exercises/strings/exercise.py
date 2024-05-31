# Determine the length of the string "These aren't the droids you're looking for.".

print(len("These aren't the droids you're looking for."))

# Convert the string 'confetti floating everywhere' to all upper case.

print('confetti floating everywhere'.upper())

# Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. Print true if the values are the same; print false if they aren't. Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.

name = "Roger"

print(name.casefold() == "RoGer".casefold())


# How can you assign the following rhyme to a single variable while preserving the line break?

s = '''
A pirate I was meant to be!
Trim the sails and roam the sea!
'''

print(s)

# Write code that checks whether the string char_sequence contains the character x.

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print('x' in char_sequence)

# Write a function that checks whether a string is empty or not. For example:


def is_empty(s):
  return len(s) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:

def is_empty_or_blank(s):
  return is_empty(s) or is_empty(s.strip(" "))

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

s = 'launch school tech & talk'

print(" ".join(list(map(lambda s: s.capitalize(), s.split()))))

# Write a function that checks whether a string starts with a specific prefix.

def starts_with(word, s):
  s_len = len(s)
  return word[:s_len] == s

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

def count_substrings(word, s):
  return word.count(s)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0




