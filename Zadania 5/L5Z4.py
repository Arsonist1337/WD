class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)


P1 = Point(0, 0)
P2 = Point(1, 1)
P3 = Point(2, 2)

print(P1.counter)
print(P2.counter)
print(P3.counter)
print("****")
P1.update(1)
print(P1.counter)
print(P2.counter)
print(P3.counter)
print("****")
P2.update(1)
print(P1.counter)
print(P2.counter)
print(P3.counter)
print("****")
P3.update(1)
print(P1.counter)
print(P2.counter)
print(P3.counter)
