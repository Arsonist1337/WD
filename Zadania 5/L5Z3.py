class Ksztalty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, x):
        return Kwadrat(self.x + x)

    def __ge__(self, drugi):
        if (self.x >= drugi.x):
            return "Bok pierwszego kwadratu jest dluzszy lub rowny drugiemu"
        return "Bok pierwszego kwadratu jest krotszy"

    def __gt__(self, drugi):
        if (self.x > drugi.x):
            return "Bok pierwszego kwadratu jest dluzszy"
        return "Bok pierwszego kwadratu jest krotszy"

    def __le__(self, drugi):
        if (self.x <= drugi.x):
            return "Bok pierwszego kwadratu jest krotszy lub rowny drugiemu"
        return "Bok pierwszego kwadratu jest dluzszy"

    def __lt__(self, drugi):
        if (self.x < drugi.x):
            return "Bok pierwszego kwadratu jest krotszy"
        return "Bok pierwszego kwadratu jest dluzszy"


Kw1 = Kwadrat(5)
Kw2 = Kwadrat(6)
Kw3 = Kwadrat(7)
print(Kw1 >= Kw2)
print(Kw1 > Kw2)
print(Kw1 <= Kw2)
print(Kw1 < Kw2)
print(Kw1 >= Kw3)
print(Kw1 > Kw3)
print(Kw1 <= Kw3)
print(Kw1 < Kw3)
print(Kw2 >= Kw3)
print(Kw2 > Kw3)
print(Kw2 <= Kw3)
print(Kw2 < Kw3)
