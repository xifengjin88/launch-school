for num in range(0, 11, 2): # 0 2 4 6 8 10
    print(num)

for i in range(10, 0, -1):
    print(i)
print("Launch!")

greeting = 'Aloha!'

for _ in range(3):
    print(greeting)

# Write a for loop that iterates over the integers from 1 to 100 and prints the result of multiplying each integer by 2.

for i in range(1, 101):
    print(i * 2)

# Using the code below as a starting point, write a while loop that prints the elements of lst at each index and terminates after printing the last element of the list.



lst = [1, 3, 7, 15]
index = 0
while index < len(lst):
    print(lst[index])
    index += 1

# Your friends just showed up! Given the following list of names, use a for loop to greet each friend individually.

friends = ['Sarah', 'John', 'Hannah', 'Dave']

for friend in friends:
    print(f"Hello, {friend}!")
  
# Write a for loop that iterates over the elements of the list cities and prints the length of each string. If the element is None, use the continue statement to skip forward to the next iteration without printing anything.

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue
    print(city)


# Loop over the elements of the fish_list list below, logging each one. Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == "Nemo":
        break



# Modify the following code so the loop continues iterating until the user inputs 'yes'.


while True:
    print('Should I stop looping?')
    answer = input()
    if answer == "yes":
        break






