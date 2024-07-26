def invert_dict(dic):
    return {value: key for key, value in dic.items()}


def keep_keys(dic, keys):
    return {key: value for key, value in dic.items() if key in keys}


VOWELS = 'aeiouAEIOU'


def remove_vowels(str_list):
    return ["".join([char for char in s if not (char in VOWELS)]) for s in str_list]


def word_lengths(s=""):
    return [f"{word} {len(word)}" for word in s.split()]


def multiply_items(lst1, lst2):
    return [a * b for a, b in zip(lst1, lst2)]


def sum_of_sums(lst):
    return sum([sum(lst[:i + 1]) for i in range(len(lst))])


def sum_digits(num):
    return sum([int(digit) for digit in str(num)])


# def staggered_case(s):
#     return "".join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(s)])

def staggered_case(s):
    should_capitalized = True
    new_str = ""
    for char in s:

        if char.isalnum():
            if should_capitalized:
                new_str += char.upper()
                should_capitalized = False
            else:
                new_str += char.lower()
                should_capitalized = True
        else:
            new_str += char

    return new_str


def unique_sequence(lst):
    seen = set()
    result = []
    for num in lst:
        if not (num in seen):
            result.append(num)
            seen.add(num)

    return result




