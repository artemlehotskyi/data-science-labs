import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

mask_female = df["Sex"] == "female"
mask_age = (df["Age"] >= 10) & (df["Age"] <= 70)
mask_fare = (df["Fare"] >= 70) & (df["Fare"] <= 100)
mask_all = mask_female & mask_age & mask_fare

names = df.loc[mask_all, "Name"]
print(names)
