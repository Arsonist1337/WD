# Zadanie 3

with open("pp4.txt", "w+") as plik:
    plik.writelines("Ala ma trzy koty tym razem, ale zaden kot nie ma Ali")
    plik.writelines("\nLinijka 2")
    plik.writelines("\nLinijka 3")
    for linia in plik:
        print(linia, end="")
with open("pp4.txt", "w+") as plik:
    a = plik.readlines()
    print(a)
