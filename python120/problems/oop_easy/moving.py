class WalkableMixin:
    def walk(self):
        return f"{self.name} {self.gait()} forward"


class Noble(WalkableMixin):
    def __init__(self, name, title):
        self._name = name
        self._title = title

    def gait(self):
        return "struts"

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    def walk(self):
        return f"{self._title} {self.name} {self.gait()} forward"


class Person(WalkableMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"


class Cat(WalkableMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"


class Cheetah(WalkableMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"


if __name__ == "__main__":
    mike = Person("Mike")
    print(mike.walk())  # Expected: "Mike strolls forward"

    kitty = Cat("Kitty")
    print(kitty.walk())  # Expected: "Kitty saunters forward"

    flash = Cheetah("Flash")
    print(flash.walk())  # Expected: "Flash runs forward"

    byron = Noble("Byron", "Lord")
    print(byron.walk())  # "Lord Byron struts forward"
    print(byron.name)  # "Byron"
    print(byron.title)  # "Lord"
