# class Organization:
#     def __init__(self, name):
#         self.id = "some_uuid"
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         self._name = name
#
#
# org = Organization("launchschool")
#
# print(org.get_name())
#

class Foo:
    nums = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @classmethod
    def create_foo(cls, name):
        foo = cls(name)
        cls.nums.append(foo)
        return foo


#
#
# f = Foo.create_foo('xifeng')
# m = Foo.create_foo('marshalee')
# print(Foo.nums)
# # print(f.nums)
# print(f.nums.append("something"))
# print(Foo.numss)


# class Test:
#     counter = 0
#
#     def __init__(self):
#         self.__class__.counter += 1
#
#     def do_something(self):
#         print(self.__class__.__name__, "doing something")
#
#
# class ChildTest(Test):
#     def do_something(self):
#         super().do_something()
#         print(self.__class__.__name__, "doing something")
#

class Car:
    def __init__(self, make, year, color):
        self._year = year
        self._color = color

        self._make = make
        self._speed = 0
        self._is_engine_on = False

    def __str__(self):
        return f"{self._make} {self._year} {self._color}"

    def __repr__(self):
        return f"Car('{self._make}', '{self.year}', '{self._color}')"

    def turn_on_engine(self):
        self._is_engine_on = True
        print("Car is turned on")

    def turn_off_engine(self):
        self.brake(self._speed)
        self._is_engine_on = False

        print("Car is turned off")

    def accelerate(self, speed):
        if self._is_engine_on:
            self._speed += speed
            print(f"Speeding up: {self._speed}")

    def brake(self, number):
        if self._is_engine_on and self._speed - number >= 0:
            self._speed -= number
            print(f"Slowing down: {number}")

        if self._speed == 0:
            print("The car has stopped completely")

    @property
    def year(self):
        return self._year

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    def speedometer(self):
        print(f"Current speed: {self._speed}")

    def paint_car(self, color):
        self.color = color

    @classmethod
    def gas_mileage(cls, gallons, miles):
        mileage = miles / gallons
        print(f'{mileage} miles per gallon')


vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
c = eval(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')



class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0 or not name.isalpha():
            raise ValueError("Name must be alphabetic.")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        Person.validate_name(first_name)
        self._first_name = first_name.title()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        Person.validate_name(last_name)
        self._last_name = last_name.title()

    @property
    def name(self):
        return f"{self.first_name} {self._last_name}"

    @name.setter
    def name(self, name):
        first_name, last_name = name
        Person.validate_name(first_name)
        Person.validate_name(last_name)
        self.first_name = first_name
        self.last_name = last_name


class Person:
    def full_name(self):      # Modify this method
        pass

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

mike = Person()
mike.first_name = 'Michael'
mike.last_name = 'Garcia'
print(mike.full_name)