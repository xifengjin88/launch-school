# Write a function that returns the first element of a list provided as an argument. For example:

def is_empty(ls):
  return len(ls) == 0

def first(ls):
  return None if is_empty(ls) else ls[0]

print(first(['Earth', 'Moon', 'Mars']))  # Earth

# Write a function that returns the last element of a list provided as an argument. For example:

def last(ls):
  return None if is_empty(ls) else ls[len(ls) - 1]

print(last(['Earth', 'Moon', 'Mars']))  # Mars


energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.remove("fossil")

energy.append("geothermal")

print(energy)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(list(alphabet))

scores = [96, 47, 113, 89, 100, 102]

count = 0

for score in scores:
  if score >= 100:
    count += 1
print(count)

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for category in vocabulary:
  for word in category:
    print(word)


destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(destination, destinations):
  for d in destinations:
    if destination == d:
      return True
  return False


print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

print("-".join(passcode))

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.

while True:
  if len(grocery_list) == 0:
    break
  first = grocery_list[0]
  print(first)
  del grocery_list[0]
