
# You may modify this line

# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1)

# All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = { key: value for key,value in dict1.items() }

print(dict1         is dict2) # False
print(dict1['a']    is dict2['a']) # True
print(dict1['a'][0] is dict2['a'][0]) # True
print(dict1['a'][1] is dict2['a'][1]) # True
print(dict1['b']    is dict2['b']) # True
print(dict1['b'][0] is dict2['b'][0]) #True
print(dict1['b'][1] is dict2['b'][1]) # True



