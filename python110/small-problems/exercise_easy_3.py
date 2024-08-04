KEYS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


def alphabetic_number_sort(lst):
    return sorted(lst, key=lambda num: KEYS[num])


def merge_sets(lst1, lst2):
    return set(lst1) | set(lst2)


def intersection(lst1, lst2):
    return frozenset(lst1) & frozenset(lst2)


def order_by_value(dic):
    return sorted(list(dic.keys()), key=lambda key: dic[key])


def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)


def leading_substrings(s):
    return [s[:i] for i in range(1, len(s) + 1)]


def substrings(s):
    return sum([leading_substrings(s[i:]) for i in range(len(s))], [])


def is_palindrome(s):
    if len(s) <= 1:
        return False
    return s == s[::-1]


def palindromes(s):
    return [substr for substr in substrings(s) if is_palindrome(substr)]


def transactions_for(tid, transactions):
    return [transaction for transaction in transactions if transaction["id"] == tid]


def is_item_available(tid, transactions):
    target_transactions = transactions_for(tid, transactions)
    total = 0
    for transaction in target_transactions:
        if transaction["movement"] == "in":
            total += transaction["quantity"]
        elif transaction["movement"] == "out":
            total -= transaction["quantity"]
    return total > 0

def time_of_day(minutes):
    min_part = int(minutes % 60)
    if minutes == 60:
        min_part = 0

    return min_part


print(time_of_day(0))        # True
print(time_of_day(-3))       # True
print(time_of_day(35))       # True
print(time_of_day(-1437))    # True
print(time_of_day(3000))     # True
print(time_of_day(800))      # True
print(time_of_day(-4231))    # True




