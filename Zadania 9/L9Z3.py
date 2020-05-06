import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

wyk = df[df["Rok"] > 2012].groupby(["Plec"]).agg({"Liczba": ["sum"]})
wykres = wyk.plot.pie(subplots=True, autopct="%.2f %%")
plt.title("Chlopcy i dziewczynki z ostatnich 5 lat")
plt.show()
