import this
#pep20

imie = 'Marianna'
lista = []
for litera in imie:
        lista.append(litera.upper())
print(lista)
#rownowazne - szybsze
print([litera.upper() for litera in imie])
lista = [print(litera.upper()) for litera in imie]
print(lista)

liczba = 123456789
print(sum([int(cyfra) for cyfra in str(liczba)]))

print([2**n for n in range(5)])

lista = [
    [1, 2],
    [3, 4]]
print([element for wiersz in lista for element in wiersz if element %2 == 0])
wynik = []
for wiersz in lista:
    for element in wiersz:
        if element %2 == 0:
            wynik.append(element)
print(wynik)

imie = 'Marianna'
# klucz, wartosc = (0, 'M')
# {0: 'M', ...}
{para[0]:para[1] for para in enumerate(imie)}
slownik = {klucz:wartosc for klucz, wartosc in enumerate(imie)}
slownik[0] # klucz
print(slownik)

slow2 = {0:'M', 1: 'a', 2: 'r', 3: 'i', 4: 'a', 5: 'n', 6: 'n', 7: 'a'}
slow_odwr = {wartosc:klucz for klucz, wartosc in slownik.items()}
print(slow_odwr)

# set
litery = set(imie)
print(litery)

# rozpakowanie krotki
imie, nazwisko = ('Marian', 'Bąbel')
# też rozpakowanie
print({*range(9)})
from timeit import timeit
print(timeit("{*range(9)}", number = 10000))
print(timeit("set(range(9))", number = 10000))
print(timeit("[]", number = 10000))
print(timeit("list()", number = 10000))

kod = """
lista = [
    [1,2],
    [3,4]]
wynik = []
for wiersz in lista:
    for element in wiersz:
        if element %2 == 0:
            wynik.append(element)"""
print(timeit(stmt= kod, number=10000))

def dodaj(liczba1, liczba2):
    return liczba1 + liczba2

dodaj(2, 3)

def witaj(imie='Jan'):
    print(f'Witaj {imie}!')
witaj()
witaj('Arkadiusz')

# def witaj(imie, nazwisko = 'Kowalski'): OK
# def witaj(imie = 'Jan', nazwisko): błąd
# print(f'Witaj {imie}!')

# moduły i pakiety

# import start as s
# s.pow()

# slicing
imie = "Małgorzata"
print(imie[0]) # pierwszy
print(imie[-1]) # ostatni
print(imie[:])
print(imie[-2:])
print(imie[::-2])
# range(start, stop, step)