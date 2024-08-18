class Machine:
    def __init__(self, kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency


class WheeledVehicle(Machine):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity
                 ):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.tires = tire_list

    def tire_pressure(self, tire_index):
        self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure


class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)


class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)


class Catamaran(Machine):
    def __init__(self,
                 number_propellers,
                 number_hulls,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls


class Motorboat(Catamaran):
    def __init__(self, kilometers_per_liter,
                 liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)
