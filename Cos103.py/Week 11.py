# Analyzing an iris dataset using pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris_dataset.csv")
print(df.head(5))
print(df.info())
print(df.shape)
# Summary statistics of the dataset
print("Summary statistics of the dataset:")
print(df.describe())

print(df.drop_duplicates())
print(df.duplicated().sum())

#Visualizing the data USING matplotlib
df.plot(x="sepal_length", y="sepal_width", kind="scatter")
plt.title("Iris Dataset: Sepal Length vs Sepal Width")
plt.xlabel("Sepal length") 
plt.ylabel("Sepal width")


df.plot(x="petal_length", y="petal_width", kind="scatter")
plt.title("Iris Dataset: Petal Length vs Petal Width")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

grouped = df.groupby("species")["sepal_length"].mean()
fig,ax = plt.subplots(figsize=(8,10))
grouped.plot(kind="bar",ax=ax)
ax.set_title("Iris Dataset: Species vs Sepal length")
ax.set_xlabel("Sepal length")
plt.tight_layout()

plt.show()




