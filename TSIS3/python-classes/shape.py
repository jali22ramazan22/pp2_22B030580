class Shape:
    area = 0

    def area_(self):
        print(self.area)


class Square(Shape):
    def __init__(self, length):
        self.area = length**2

class Rectangle(Shape):
    def __init__(self, length, width):

        self.area = length * width


square = Square(4)
rec = Rectangle(3, 4)
rec.area_()
square.area_()

