import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"[{self.x}, {self.y}]")

    def move(self, x_, y_):
        self.x += x_
        self.y += y_

    def dist(self, point2):
        print(f"{math.sqrt((self.x - point2.x)**2 + (self.y - point2.y)**2)}")

