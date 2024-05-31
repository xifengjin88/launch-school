car = {
  "type": "sedan",
  "color": "blue",
  "mileage": 80_000
}

car["year"] = 2003

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

del car["mileage"]

print(car["color"])

print(len(car))

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for number in numbers.values():
  half_numbers.append(number // 2)


print(half_numbers)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
  print(f"A {key} number is {value}")