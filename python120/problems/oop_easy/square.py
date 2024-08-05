from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)



if __name__ == '__main__':
    square = Square(3)
    print(square.area == 9)