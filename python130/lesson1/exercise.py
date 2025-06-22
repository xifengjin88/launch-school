import collections
from functools import reduce

Card = collections.namedtuple("Card", ["rank", "suit"])


class Deck:
    ranks = [str(rank) for rank in range(2, 11)] + list("JQKA")
    suits = ["clubs", "diamonds", "hearts", "spades"]

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, i):
        return self._cards[i]


deck = Deck()

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def sort_order(card):
    rank_value = Deck.ranks.index(card.rank)
    suit = card.suit

    return suit_values[suit] * 13 + rank_value


def high_spades(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def square(nums):
    return list(map(lambda num: num * num, nums))


def even(num):
    return num % 2 == 0


def product(acc, num):
    return acc * num


# print(reduce(product, [1,2,3,4, 5], 1))
#
#
# print(list(map(lambda s: len(s), ["abc", "oke"])))
#
# print(list(filter(lambda a: a is not None, [1,2,3, None])))
#
# print(reduce(lambda acc, s: acc + s, ["a", "b", "c"]))

def flatten_list(items):
    if items:
        for item in items:
            if isinstance(item, list):
                yield from flatten_list(item)
            else:
                yield item


def greet(name, message, punctuation="."):
    return f"{message}, {name}{punctuation}"


def create_user(username, /, *, email, age):
    return {"username": username, "email": email, "age": age}
print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}

def build_profile(first_name, last_name, **kargs):
    return { "first_name": first_name, "last_name": last_name, **kargs}


print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))


def concatenate(*strings):
    return " ".join(strings)


print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course

def display_info(data, /, *, reverse = False, uppercase = False):
    result = data
    if reverse:
        result = result[::-1]
    if uppercase:
        result = result.upper()
    return result


print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC

lst = [10, 20, 30, 40]

a, b, c, d = lst

data = (100, 200, 300, 400)

numbers = [1, 2, 3, 4, 5, 6]

first, second, *rest = numbers

print(first, second, rest)


data = ((1, 2), (3, 4), (5, 6))

((a, b), (c, d), (e, f)) = data

def longest_sentence(words):
    sentences = []
    sentence = ""
    for char in words:
        if char in [".", "?", "!"] and sentence:
            sentences.append(sentence + char)
            sentence = ""
        else:
            sentence += char
    longest_sentence = max(sentences, key=lambda sentence: len(sentence.split()))
    print(longest_sentence.strip())
    print(len(longest_sentence.split()))


long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.



