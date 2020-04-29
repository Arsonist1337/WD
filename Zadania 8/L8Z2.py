import pandas as pd

# Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)

# Zadanie 2 a - ponad 1k na rok
print(df[df['Liczba'] > 1000])

# Zadanie 2 b - moje imię
print(df[df['Imie'] == 'MICHAŁ'])

# Zadanie 2 c - suma dzieci
print(df.agg({'Liczba': ['sum']}))

# Zadanie 2 d - suma dzieci z lat 2000-2005
print(df[df['Rok'] < 2006].agg({'Liczba': ['sum']}))

# Zadanie 2 e - suma chłopców i suma dziewczynek
print(df[df['Plec'] == 'M'].agg({'Liczba': ['sum']}))
print(df[df['Plec'] == 'K'].agg({'Liczba': ['sum']}))

# Zadanie 2 f - najpopularniejsze imiona na rok
dfdrugi = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(dfdrugi, start=1):
    print(f" {index} {group[0]}")
    print(f" {group[1].iloc[0]['Imie']}", end=' ')
    print(f" {group[1].iloc[0]['Liczba']}")

# Zadanie 2 g - najpopularniejsze imię chłopca i dziewczynki
print("##########")
print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']})
        .sort_values(('Liczba', 'sum'), ascending=False).iloc[[0, 1]])
