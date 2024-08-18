class Car:
    manufacturer = "class_manufacturer"

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(self.__class__.manufacturer)
        print(self.manufacturer)


if __name__ == "__main__":
    c = Car("car manufacturer")
    c.show_manufacturer()
