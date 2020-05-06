import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)

wyk = df.groupby(["Plec"]).agg({"Liczba": ["sum"]})
wykres = wyk.plot.bar()
plt.ylabel("Liczba urodzonych")
plt.xlabel("Plec")
plt.legend()
plt.title("Liczba urodzonych wedlug plci")
plt.show()
