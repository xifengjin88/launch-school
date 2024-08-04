class Vehicle:
    count = 0

    def __init__(self):
        Vehicle.count += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.count

class SignalMixin:
    def signal_off(self):
        print("Signal is off")

    def signal_on(self):
        print("Signal is on")

    def signal_left(self):
        print("signalling left")

    def signal_right(self):
        print("signalling right")


class Car(SignalMixin, Vehicle):
    pass


class Truck(SignalMixin, Vehicle):
    pass


class Boat(Vehicle):
    pass


if __name__ == '__main__':
    # print(Car.vehicles())  # 0
    # car1 = Car()
    # print(Car.vehicles())  # 1
    # car2 = Car()
    # car3 = Car()
    # car4 = Car()
    # print(Car.vehicles())  # 4
    # truck1 = Truck()
    # truck2 = Truck()
    # print(Truck.vehicles())  # 6
    # boat1 = Boat()
    # boat2 = Boat()
    # print(Boat.vehicles())  # 8
    car1 = Car()
    truck1 = Truck()
    boat1 = Boat()
    #
    # car1.signal_left()  # Signalling left
    # truck1.signal_right()  # Signalling right
    # car1.signal_off()  # Signal is now off
    # truck1.signal_off()  # Signal is now off

    print(Car.mro())
    print()
    print(Truck.mro())
    print()
    print(Boat.mro())
    print()
    print(Vehicle.mro())
    print()
