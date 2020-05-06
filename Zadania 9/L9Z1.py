import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)

wyk = df.groupby(["Rok"]).agg({"Liczba": ["sum"]})
wykres = wyk.plot()
plt.ylabel("Liczba urodzonych")
plt.xlabel("Rok")
plt.legend()
plt.title("Liczba urodzonych wedlug roku")
plt.show()
