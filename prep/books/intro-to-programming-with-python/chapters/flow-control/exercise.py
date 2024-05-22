# False or (True and False) -> False
# True or (1 + 2) -> True
# (1 + 2) or True -> 3
# True and (1 + 2) -> 3
# False and (1 + 2) -> False
# (1 + 2) and True -> True
# (32 * 4) >= 129 -> False
# False != (not True) -> False
# True == 4 -> False
# False == (847 == '847') -> True

def even_odd(num):
  print('even' if num % 2 == 0 else 'odd')


# return ('bar' if foo() else qux()) -> 

# if foo():
#   return 'bar'
# else:
#   return qux()


def capitalize(s):
  if len(s) > 10:
    return s.upper()
  return s

print(capitalize("hello world"))
print(capitalize("goodbye"))

def number_range(num):
  if num < 0:
    print(f"{num} is less than 0.")
  elif num <= 50:
    print(f"{num} is between 0 and 50")
  elif num <= 100:
    print(f"{num} is between 51 and 100")
  else:
    print(f"{num} is greater than 100")


number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0


    