import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

#1
mask_female = df["Sex"] == "female"
mask_age = (df["Age"] >= 10) & (df["Age"] <= 70)
mask_fare = (df["Fare"] >= 70) & (df["Fare"] <= 100)
mask_all = mask_female & mask_age & mask_fare

names = df.loc[mask_all, "Name"]
print(names)

#2

df["Pclass"] = df["Pclass"].replace({1: 'First', 2: 'Second', 3: 'Third'})

#3

df_crimes = pd.read_excel('CrimesData.xlsx')

df_crimes.info()
df_crimes['CrimeDate'] = pd.to_datetime(df_crimes['CrimeDate'], format='%m/%d/%Y')
YEAR = 2012
mask_year = df_crimes['CrimeDate'].dt.year == YEAR

crimes_year = df_crimes.loc[mask_year]
crimes_year['CrimeDate'].dt.month.value_counts().sort_index()