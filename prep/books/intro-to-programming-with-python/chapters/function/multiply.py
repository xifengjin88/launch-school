'''

Write a program that uses a multiply 
function to multiply two numbers and returns the result. 
Ask the user to enter the two numbers, then output the numbers and 
result as a simple equation.
'''

def multiply(a, b):
  return a * b


a = input("Enter the first number: ")
b = input("Enter the second number: ")

print(f"{a} * {b} = {multiply(float(a), float(b))}")


