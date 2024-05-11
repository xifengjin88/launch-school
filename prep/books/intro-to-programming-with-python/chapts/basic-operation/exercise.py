'''
Concatenate two strings, one with your first name and one with your last
to create a new string with your full name as its value. For example, 
if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.
'''

first_name = "xifeng"
last_name = "jin"

full_name = first_name + " " + last_name

print(full_name)

digits = 4936

print(f"One place is {digits % 10}.")

digits //= 10

print(f"Tens place is {digits % 10}.")

digits //= 10

print(f"Hundreds place is {digits % 10}.")

digits //= 10

print(f"Thousands place is {digits % 10}.")

print('5' + '10') # this code will print 510, because it's a string concatenation operation

print(int('5') + int('10'))
