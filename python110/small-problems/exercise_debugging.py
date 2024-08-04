# def decrease(counter):
#     return counter - 1
#
# counter = 10
#
# for _ in range(10):
#     print(counter)
#     counter = decrease(counter)
#
# print('LAUNCH!')

# def reverse_string(string):
#     for char in string:
#         string = char + string
#
#     return string[:(len(string) // 2)]
# print(reverse_string("hell"))


# def multiply_list(lst):
#     for i, item in enumerate(lst):
#         lst[i] = item * 2
#
#     return lst
#
# print(multiply_list([1, 2, 3]) == [2, 4, 6])

# def get_key_value(my_dict, key):
#     if key in my_dict:
#         return my_dict[key]
#     else:
#         return None
#
# print(get_key_value({"a": 1}, "b"))

# events = {
#     "2023-08-13": ["Python debugging exercises"],
#     "2023-08-14": ["Read 'Automate the Boring Stuff'"],
#     "2023-08-15": ["Webinar: Python for Data Science"],
# }
#
# def is_date_available(date):
#     return not( date in events)
# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True



# def append_to_list(value, lst):
#     lst.append(value)
#     return lst
#
# print(append_to_list(1, []) == [1])
# print(append_to_list(2, []) == [2])

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed



