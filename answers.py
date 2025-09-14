import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

#load dataset
try:
    df=pd.read_csv("iris.csv")
    print("Data loaded successfully")
except FileNotFoundError:
    print("iris.csv not found")
except Exception as e:
    print(f"rror loading dataser: {e}")
# Display first few rows
print(df.head())

# check data structure
print (df.info())

# Check for missing values
print(df.isnull().sum())

# clean data id missing values exist

df=df.dropna()
print("missing values dropped")

# Task 2
# summary statistics
print("\nBasic statistics:")
print(df.describe())

# Grouping data
grouped=df.groupby("species")["petal_length"].mean()
print("\nMean petal length per species:")
print(grouped)

# Task 3
# Line chart 
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="blue")
plt.title("Line chart of sepal length over index")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.legend()
plt.show()

# Bar chart
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal_length", data=df, ci=None, palette="viridis")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (avg)")
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["sepal_width"], bins=20, color="orange", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()

# scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title="Species")
plt.show()