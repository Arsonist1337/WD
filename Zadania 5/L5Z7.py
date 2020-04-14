class Wlasny:
    """Iterator zwracający tylko elementy z parzystych
    indeksów przekazanej kolekcji"""
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 2
        return self.data[self.index]


slowo = "Kwadrat"
Parzyste = Wlasny(slowo)
print(Parzyste.__next__())
print(Parzyste.__next__())
print(Parzyste.__next__())
print("-----------")
ciag = [1, 2, 3, 4, 5]
Parzyste2 = Wlasny(ciag)
print(Parzyste2.__next__())
print(Parzyste2.__next__())
