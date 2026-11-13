import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

mask_female = df["Sex"] == "female"
mask_age = (df["Age"] >= 10) & (df["Age"] <= 70)
print(mask_age.head())
print(mask_age.sum())