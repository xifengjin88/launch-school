class Mammal:
    LEGS = 4


class Human(Mammal):
    LEGS = 2


if __name__ == '__main__':
    h = Human()
    print(h.__class__.LEGS)



