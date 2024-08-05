class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

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

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string")
        # print(name)
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ""
        if len(parts) > 1:
            self.last_name = parts[1]


if __name__ == '__main__':
    bob = Person('Robert')
    print(bob.name)  # Robert
    print(bob.first_name)  # Robert
    print(repr(bob.last_name))  # ''
    bob.last_name = 'Smith'
    print(bob.name)  # Robert Smith

    bob.name = 'Prince'
    print(bob.first_name)  # Prince
    print(repr(bob.last_name))  # ''

    bob.name = 'John Adams'
    print(bob.first_name)  # John
    print(bob.last_name)  # Adams
