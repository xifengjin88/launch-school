# Without looking at your notes or the official documentation, try to recall all values that count as falsy in Python.

# 0, "", {}, set(), [], False, None -> Falsy

# The code provided below randomly initializes random_number to either 0 or 1 each time it is executed.

# Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0

import random
random_number = random.randint(0, 1)

if random_number == 1:
  print("Yes")
else:
  print("No")

# Rewrite your code from the previous exercise to use a ternary expression.

print("Yes") if random_number == 1 else print("No")

# Initialize a variable weather with a string value being 'sunny', 'rainy', or 
# whatever weather condition you choose. Then, write an if statement that prints:


# It's a beautiful day! if weather's value is 'sunny'
# Grab your umbrella. if weather's value is 'rainy'
# Let's stay inside. if weather's value is anything else

weather = "no"

if weather == "sunny":
  print("It's a beautiful day!")
elif weather == "rainy":
  print("Grab your umbrella.")
else:
  print("Let's stay inside.")

# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. Feel free to add more cases besides 'sunny' and 'rainy'.

match weather:
  case "sunny":
    print("It's a beautiful day!")
  case "rainy":
    print("Grab your umbrella.")
  case _:
    print("Let's stay inside.")


if False or True:
    print('Yes!')
else:
    print('No...')


sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

