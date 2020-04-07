class Slowa:

    slowo1 = ""
    slowo2 = ""

    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2

    def wyswietl_wyrazy(self):
        print(f"{self.slowo1} {self.slowo2}")

    def sprawdz_czy_palindrom(self):
        return self.slowo1 == self.slowo2[::-1]

    def sprawdz_czy_metagramy(self):
        if len(self.slowo1) == len(self.slowo2):
            r = 0
            for i in range(0, len(self.slowo1)):
                if self.slowo1[i] != self.slowo2[i]:
                    r += 1
            if r == 1:
                return True
            return False
        return False

    def sprawdz_czy_anagramy(self):
        if len(self.slowo1) != len(self.slowo2):
            return False
        slowo1_list = list(self.slowo1)
        slowo1_list.sort()
        slowo2_list = list(self.slowo2)
        slowo2_list.sort()
        return slowo1_list == slowo2_list


slowo = Slowa("kajak", "kajak")
slowo.wyswietl_wyrazy()
print(slowo.sprawdz_czy_palindrom())
print(slowo.sprawdz_czy_metagramy())
print(slowo.sprawdz_czy_anagramy())
