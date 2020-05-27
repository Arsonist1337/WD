import matplotlib.pyplot as plt
import pandas as pd

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

dane_wykres1 = df.groupby("Plec")["Liczba"].sum().reset_index()
dane_wykres2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres2K = dane_wykres2[dane_wykres2["Plec"] == "K"].reset_index()
dane_wykres2M = dane_wykres2[dane_wykres2["Plec"] == "M"].reset_index()
dane_wykres2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres3 = df.groupby("Rok")["Liczba"].sum().reset_index()

plt.subplot(131)
plt.bar(dane_wykres1["Plec"], dane_wykres1["Liczba"],
        color=["orange", "yellow"])
plt.xlabel("Plec")
plt.ylabel("Liczba urodzonych")

plt.subplot(132)
plt.bar(dane_wykres2K["Rok"], dane_wykres2K["Liczba"], color="blue", label="K")
plt.bar(dane_wykres2M["Rok"], dane_wykres2M["Liczba"], color="red", label="M",
        bottom=dane_wykres2K["Liczba"])
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")
plt.legend()

plt.subplot(133)
plt.bar(dane_wykres3["Rok"], dane_wykres3["Liczba"], color="c")
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")

plt.suptitle("Liczba urodzonych K i M")
plt.show()
