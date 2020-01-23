import math

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f'Vec({self.x}, {self.y})'

    def plus(self, vec):
        return Vec(self.x + vec.x, self.y + vec.y)

    def minus(self, vec):
        return Vec(self.x - vec.x, self.y - vec.y)


vec1 = Vec(3, 4)
print(vec1.plus(Vec(3, 4)))
print(vec1.length)
print(vec1.minus(Vec(2, 3)))