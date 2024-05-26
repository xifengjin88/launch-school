r = range(0, 25, 3)

print(list(r)[6])

s = 'Launch School'

index = s.find('c')

if index != -1:
  print(s[index:index + 6])


s = (1,2,3,4,5)

print(tuple(reversed(s))[1:len(s) - 1])


pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}


print(pets["Dog"])
print(pets.get("Lizard"))
print(pets.get("Lizard", "<silence>"))

print('abc-def'.isalpha()) # False
print('abc_def'.isalpha()) # False
print('abc def'.isalpha()) # False
print('abc def'.isalpha() and 
      'abc def'.isspace()) # False
print('abc def'.isalpha() or 
      'abc def'.isspace()) # False
print('abcdef'.isalpha()) # True
print('31415'.isdigit()) #True
print('-31415'.isdigit()) # True
print('31_415'.isdigit()) #False
print('3.1415'.isdigit()) #True
print(''.isspace())  #False

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print("+".join(info.split("*")))

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606

print(stuff)

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats["Pete"]["Cocoa"]["enjoys"])

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(list(zip(my_str, my_list, my_tuple, my_range)))