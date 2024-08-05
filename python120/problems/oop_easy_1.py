# print("Hello")                # <class 'str'>
# print(5)                      # <class 'int'>
# print([1, 2, 3])              # <class 'list'>

print(type("Hello"))
print(type(5))
print(type([1, 2, 3]))


class Cat:
    count = 0
    COLOR = "purple"
    def __init__(self, name="John Doe"):
        self.name = name
        Cat.count += 1
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def greet(self):
        print(f"Hello, my name is {self.name} and I am a {Cat.COLOR} cat.")

    @classmethod
    def generic_greeting(cls):
        print("Hi, I am a cat")

    def rename(self, new_name):
        self.name = new_name

    def identify(self):
        return self

    @classmethod
    def total(cls):
        return Cat.count



Cat.total()         # 0

kitty1 = Cat()
print(Cat.total())         # 1

kitty2 = Cat()
print(Cat.total())         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
print(Cat.total())         # 3
