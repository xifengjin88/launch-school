class TowableMixin:
    def tow(self):
        print("I can tow a trailer!")


class Car:
    pass


class Vehicle:
    def start_engine(self):
        return 'Ready to go!'


class Truck(TowableMixin, Vehicle):
    def start_engine(self, speed):
        return f"{super().start_engine()} Drive {speed}, please!"


class WalkingMixin:
    def walk(self):
        print("Let's go for a walk")


class Cat(WalkingMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")


# Comments show expected output
truck1 = Truck()
truck1.tow()  # I can tow a trailer!

# car1 = Car()
# car1.tow()
# # AttributeError: 'Car' object has no attribute 'tow'
