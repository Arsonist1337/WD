print("Hello world!")

tekst1 = "Hello world!"
tekst2 = """Hello 
       :)
world!"""
tekst3 = 'Hello world!'
#komentarz
print(tekst2)
print(tekst3)
print(type(tekst3))
tekst3=12
print(tekst3)
print(type(tekst3))
print(type(2.5))
print(type(True))
print(type(None))

print(5+5)
print(5-3)
print(5*5)
print(5/4)
print(5//4) #dzielenie bez reszty
print(5%3) #modulo, jak c++
print(5**5) #potegowanie

print("Ala "+"ma kota.") #konkatynacja (concat)
# print("Ala "+"ma "+5+" lat")                      #BLAD
print("Ala "+"ma "+str(5)+" lat") # poprawne mieszanie typów
liczba = int("100")
print(liczba)
print("Binarnie: "+str(bin(liczba)[2:])) #dec to bin

#===============================listy==============================
lista = []
print(type(lista))
lista2 = [1,2,3]
print(lista2[0])
imie="Jan"
print(imie[0])
lista2[0]=5
# imie[0]="P"                     #BLAD stringi sa niemutowalne
imie="Pan" #poprawne
imie=imie.swapcase()
imie.swapcase() #zamienia, ale nie zapisuje zmian!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(imie)
print(imie.count("A"))
"Ala".swapcase()
lista2.append(1) #dodaje element na koniec listy
lista3=[1,"Ala",4.5,None,True,[1,2]]
print(lista3[5][1])

macierz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(macierz[2][1])
nowa = lista2 + macierz

#===============================słownik================================
slownik={}
slownik['imie']='Adam'
slownik[0]='Adam'
slownik[1]='Adam'
i=1
slownik[i]='Mariola'
print(slownik)
slownik2={0: 'Adam', 2: 'Hadam', 1: 'Mariola'}
print(slownik2)
print(slownik2.keys())
print(slownik2.values())

def pow():
    pass

#for element in kolekcja:
    #akcja w for'ze
#akcja poza for'em

# from math import *

# pow() #wywola sie pow z math'a

import math as m
m.pow()

from math import pow as npow
npow(2,5)

from math import sin