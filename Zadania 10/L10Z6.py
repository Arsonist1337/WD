import matplotlib.pyplot as plt
import pandas as pd

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

dane_wykres = df.groupby("Plec")["Liczba"].sum().reset_index()
dane_wykres2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres2K = dane_wykres2[dane_wykres2["Plec"] == "K"].reset_index()
dane_wykres2M = dane_wykres2[dane_wykres2["Plec"] == "M"].reset_index()
dane_wykres2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres3 = df.groupby("Rok")["Liczba"].sum().reset_index()

plt.subplot(131)
plt.bar(dane_wykres["Plec"], dane_wykres["Liczba"], color=["orange", "yellow"])
plt.xlabel("Plec")
plt.ylabel("Liczba urodzonych")

plt.subplot(132)
plt.plot(dane_wykres2K["Rok"], dane_wykres2K["Liczba"])
plt.plot(dane_wykres2M["Rok"], dane_wykres2M["Liczba"])

plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")

plt.subplot(133)
plt.bar(dane_wykres3["Rok"], dane_wykres3["Liczba"], color="c")
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")

plt.suptitle("Liczba urodzonych K i M")
plt.show()
