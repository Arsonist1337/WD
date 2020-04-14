class Wlasny:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        for i in "AaEeIiOoUuYy":
            if self.data[self.index + 1] == i:
                self.index += 1
                return self.data[self.index]
        self.index += 1
        return self.__next__()


slowo = "Kwadrat"
samogloska = Wlasny(slowo)
print(samogloska.__next__())
print(samogloska.__next__())
