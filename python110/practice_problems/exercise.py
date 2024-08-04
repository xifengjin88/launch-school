import string
from math import sqrt


def smaller_numbers_than_current(nums):
    result = []
    for i, num in enumerate(nums):
        count = set()
        for j, inner_num in enumerate(nums):
            if i != j and inner_num < num:
                count.add(inner_num)
        result.append(len(count))
    return result


def minimum_sum(nums):
    if len(nums) < 5:
        return None
    result = float('inf')

    for i in range(len(nums) - 5 + 1):
        s = sum(nums[i:i + 5])
        if s < result:
            result = s
    return result


def to_weird_case(s):
    new_words = []
    words = s.split()
    count = 1

    def process_word(word):
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 1:
                new_word += word[i].upper()
            else:
                new_word += word[i]
        return new_word

    for word in words:
        if count >= 3:
            count = 1
            new_words.append(process_word(word))
        else:
            count += 1
            new_words.append(word)
    return " ".join(new_words)


def closest_numbers(nums):
    shortest_distance = float('inf')
    pair = None
    for i in range(len(nums) - 1):
        a = nums[i]
        for j in range(i + 1, len(nums)):
            b = nums[j]
            distance = abs(a - b)
            if distance < shortest_distance:
                shortest_distance = distance
                pair = (a, b)
    return pair


def most_common_char(s):
    count = {}
    most_frequent_char = None
    most_frequent_count = float("-inf")
    s = s.lower()
    for char in s:

        count[char] = count.get(char, 0) + 1

        if count[char] > most_frequent_count or (
                count[char] == most_frequent_count and most_frequent_char is not None and (
                s.index(char) < s.index(most_frequent_char))
        ):
            most_frequent_char = char

            most_frequent_count = count[char]

    return most_frequent_char


def count_letters(s):
    count = {}
    for char in s:
        if char.islower():
            count[char] = count.get(char, 0) + 1
    return count


def pairs(nums):
    if len(nums) < 2:
        return 0
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1
    return sum(list([value // 2 for value in seen.values()]))


def is_vowel(s):
    return all([char in ["a", "e", "i", "o", "u"] for char in s])


def longest_vowel_substring(s):
    longest_vowel_substring = ""

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]

            if is_vowel(substring) and len(substring) > len(longest_vowel_substring):
                longest_vowel_substring = substring
    return len(longest_vowel_substring)


def count_substrings(s, target):
    count = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]

            if substring == target:
                if count:
                    last_i, last_j = count[-1]

                    if i >= last_j:
                        count.append((i, j))
                else:
                    count.append((i, j))

    return len(count)


def even_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if int(substring) % 2 == 0:
                count += 1
    return count


def substrings(s):
    return [
        s[i:j] for i in range(0, len(s))
        for j in range(i + 1, len(s) + 1)
    ]


def repeated_substring(s):
    substrs = sorted(substrings(s), key=lambda sb: len(sb))

    for i in range(len(s), 0, -1):
        for sub in substrs:

            if sub * i == s:
                return sub, i


def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    for char in s:
        char = char.lower()
        if char in alphabet:
            alphabet.remove(char)
    return len(alphabet) == 0


def unscramble(s, target):
    count = {}
    for char in target:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if char in count:
            count[char] = count[char] - 1
            if count[char] == 0:
                del count[char]
    return len(count) == 0


def seven_eleven(num):
    return sum([i for i in range(num) if i % 7 == 0 or i % 11 == 0])


def get_product(s):
    a, b, c, d = s
    return int(a) * int(b) * int(c) * int(d)


def greatest_product(digits):
    products = [get_product(s) for s in substrings(digits) if len(s) == 4]
    return max(products)


def distinct_multiples(s):
    count = {}
    for char in s:
        char = char.lower()
        count[char] = count.get(char, 0) + 1
    return len([value for key, value in count.items() if value > 1])


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1


def nearest_prime_sum(nums):
    s = sum(nums)
    next_prime = get_next_prime(s)

    return next_prime - s


def equal_sum_index(nums):
    for i in range(len(nums)):
        left = nums[:i]
        right = nums[i + 1:]
        if sum(left) == sum(right):
            return i
    return -1


def odd_fellow(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1

    return [key for key, value in count.items() if value % 2 == 1][0]


def what_is_different(nums):
    for n in nums:
        if nums.count(n) == 1:
            return n


