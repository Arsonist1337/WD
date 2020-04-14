class Material:

    rodzaj = ""
    dlugosc = 0
    szerokosc = 0

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return "{}".format(self.rodzaj)


class Ubrania(Material):

    rozmiar = 0
    kolor = ""
    dla_kogo = ""

    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        return "{}, {}, {}".format(self.kolor, self.dla_kogo, self.rozmiar)


class Sweter(Ubrania):

    rodzaj_swetra = ""

    def _init_(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        return "{}".format(self.rodzaj_swetra)


cos = Material("Poliester", 25, 25)
print(cos.wyswietl_nazwe())
cos2 = Ubrania("Czerwony", "Jan Kowal", 39)
print(cos2.wyswietl_dane)
cos3 = Sweter("Z golfem")
print(cos3.wyswietl_dane)
