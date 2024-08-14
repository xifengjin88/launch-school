class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)

    def __rmul__(self, value):
        return Vector(self.x * value, self.y * value)


if __name__ == '__main__':
    print(Vector(3, 2) + Vector(5, 12))  # Vector(8, 14)
    print(Vector(5, 12) - Vector(3, 2))  # Vector(2, 10)
    print(Vector(5, 12) * 2)  # Vector(10, 24)
    print(3 * Vector(5, 12))  # Vector(15, 36)

    my_vector = Vector(5, 7)
    my_vector += Vector(3, 9)  # Vector(8, 16)
    print(my_vector)

    my_vector -= Vector(1, 7)
    print(my_vector)  # Vector(7, 9)
    try:
        print(Vector(3, 2) + 5)
    except TypeError:
        print("operator not supported")
