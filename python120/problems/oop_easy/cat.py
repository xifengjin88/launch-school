class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def info(self):
        return f"My cat {self.name} is {self.age} years old and has {self.color} fur."


if __name__ == '__main__':
    cocoa = Cat('Cocoa', 3, 'black')
    cheddar = Cat('Cheddar', 4, 'yellow and white')

    print(cocoa.info)
    print(cheddar.info)
