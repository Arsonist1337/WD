import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zamowienia.csv", sep=";")

wyk = df.groupby("Sprzedawca").agg({"idZamowienia": ["count"]})
wykres = wyk.plot.bar()
plt.ylabel("Liczba zamowien")
plt.xlabel("Sprzedawca")
plt.legend()
plt.title("Zamowienia na sprzedawce")
plt.show()
