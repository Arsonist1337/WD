class Point:

    def __init__(self, x=0, y=0):
        """Konstuktor punktu."""
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


p1 = Point(1, 1)
p2 = Point(-5, 2)
p3 = p1 + p2
print(p3)
