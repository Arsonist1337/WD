import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")
print(df)

# Zadanie 3 a - unikalne nazwiska sprzedawców
print(df["Sprzedawca"].unique())

# Zadanie 3 b
# print(df.sort_values(('Utarg'), ascending=False).nth(4))

# Zadanie 3 c - suma zamowien dla sprzedawcy
print(df.groupby('Sprzedawca')['idZamowienia'].count())

# Zadanie 3 d - suma zamowien na kraj
print(df.groupby('Kraj')['idZamowienia'].count())

# Zadanie 3 e - suma zamowien 2005 dla polskich sprzedawcow
# print(df(['Kraj' == 'Polska'] & df['Data zamowienia'] >= '2005-01-01') & df['Data zamowienia'] <= '2006-01-01')['idZamowienia'].count()))

# Zadanie 3 f - srednia zamowien z roku 2004
# print(df[df["Data zamowienia"].str.contains("2004")])

# Zadanie 3 g -
# df[df["Data zamowienia"].str.contains("2004")]
#            .to_csv("zamowienia_2004.csv", index=False, sep=";")
# df[df["Data zamowienia"].str.contains("2005")]
#            .to_csv("zamowienia_2005.csv", index=False, sep=";")
