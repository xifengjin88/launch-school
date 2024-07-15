# lst = [10, 9, -6, 11, 7, -16, 50, 8]
#
# print(sorted(lst))
# print(sorted(lst, reverse=True))
#
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
#
# print(sorted(lst, key=str))
# print(sorted(lst, key=str, reverse=True))
#
# books = [
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967',
#     },
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800',
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869',
#     },
# ]
#
#
# def sort_key(book):
#     return int(book['published'])
#
#
# print(sorted(books, key=sort_key))

# lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
#
# lst2 = [
#     {
#         'first': ['a', 'b', 'c'],
#         'second': ['d', 'e', 'f']
#     },
#     {
#         'third': ['g', 'h', 'i']
#     }
# ]
#
# lst3 = [['abc'], ['def'], {'third': ['ghi']}]
#
# dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
#
# # This one is much more challenging than it looks! Try it, but don't
# # stress about it. If you don't solve it in 10 minutes, you can look
# # at the answer.
# dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
#
# print(lst1[2][1][3])
#
# print(lst2[1]["third"][0])
#
# print(lst3[2]["third"][0][0])
#
# print(dict1["b"][1])
#
# print(list(dict2["3rd"].keys())[0])
#
# lst1 = [1, [2, 3], 4]
#
# lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
#
# dict1 = {'first': [1, 2, [3]]}
#
# dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
#
# lst1[1][1] = 4
#
# lst2[2] = 4
#
# dict1["first"][2][0] = 4
#
# dict2["a"]["a"][2] = 4
#


a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

# lst -> [4, [3, 8]]
# a -> 2
# b -> [3, 8]

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# for name in munsters.keys():
#     age, gender = munsters[name]["age"], munsters[name]["gender"]
#     print(f"{name} is {age}-year-old {gender}")
#

total_age = sum([person["age"] for _, person in munsters.items() if person["gender"] == "male"])

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

print([sorted(sublist) for sublist in lst])

print([sorted(sublist, key=str) for sublist in lst])

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

print(dict(lst))

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

print(sorted(lst, key=lambda sublist: sum([item for item in sublist if item % 2 == 1])))

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

print([{key: value + 1 for key, value in obj.items()} for obj in lst])

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

print([[item for item in sublist if item % 3 == 0] for sublist in lst])


dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

print([[color.capitalize() for color in obj["colors"]] if obj["type"] == "fruit" else obj["size"].upper() for obj in dict1.values()])

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# print([obj for obj in lst if all([num % 2 == 0 for sublist in obj.values() for num in sublist])])


import random

characters = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def generate_uuid():
    return "-".join(["".join([random.choice(characters) for _ in range(pattern)]) for pattern in [8, 4, 4, 4, 12]])



dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

vowels = ["a", "e", "i", "o", "u"]

# print([char for lst in dict1.values() for word in lst for char in word if char in vowels])

def even_values(lst):
    evens = []

    for index, value in enumerate(lst):
        print(lst, value, index)
        if value % 2 == 0:
            evens.append(value)
        item = lst.pop(0)
        print(item)

    return evens

even_values([1, 3, 4, 2, 4, 6, 5, 7, 9, 10, 12])