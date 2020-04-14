class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


slowo = "Kwadrat"
odwrot = Wspak(slowo)
print(odwrot.__next__())
print(odwrot.__next__())
print(odwrot.__next__())
print(odwrot.__next__())
print(odwrot.__next__())
print(odwrot.__next__())
print(odwrot.__next__())
print("--------")
ciag = [1, 2, 3, 4, 5]
odwrot2 = Wspak(ciag)
print(odwrot2.__next__())
print(odwrot2.__next__())
print(odwrot2.__next__())
print(odwrot2.__next__())
print(odwrot2.__next__())
