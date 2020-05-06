import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.data", sep=",", names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"])

df1 = df[df["Class"] == "Iris-setosa"]
df2 = df[df["Class"] == "Iris-versicolor"]
df3 = df[df["Class"] == "Iris-virginica"]
s1 = plt.scatter(df1["Sepal length"], df1["Sepal width"], color="purple")
s2 = plt.scatter(df2["Sepal length"], df2["Sepal width"], color="brown")
s3 = plt.scatter(df3["Sepal length"], df3["Sepal width"], color="cyan")

plt.ylabel("Sepal length")
plt.xlabel("Sepal width")
plt.title("Zadanie 4")
plt.legend((s1, s2, s3), ("Setosa", "Versicolor", "Virginica"), title="Klasy")
plt.show()
