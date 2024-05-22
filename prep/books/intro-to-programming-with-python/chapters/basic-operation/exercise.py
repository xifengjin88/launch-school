'''
Concatenate two strings, one with your first name and one with your last
to create a new string with your full name as its value. For if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.example, 

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


foo = ['a', 'b', 'c']
# print(foo[3])   this will raise an error, because index starts at 0 and 3 is out of range

# 'foo' == 'Foo' this is falsy because f and F is not the same

# print(int('3.1415')) this will raise an error

# '12' < '9' this gets evaluated as True because '9' is greater than '1' lexically
