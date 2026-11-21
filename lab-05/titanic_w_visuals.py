import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme()


df = pd.read_csv("TitanicData.csv", sep=';')
group = df.groupby(['Pclass', 'Sex'])

table = group.size().unstack()
print(table)
print(pd.crosstab(df['Sex'], df['Pclass']).T)

table.plot(kind='bar', rot=0)
plt.title('Кількість пасажирів за класом і статтю')
plt.xlabel('Клас Каюти')
plt.ylabel('Кількість пасажирів')
plt.show()

x = np.arange(len(table))
width = 0.4

plt.bar(x - width/2, table['female'], width, label='female')
plt.bar(x + width/2, table['male'], width, label='male')

plt.xticks(x, table.index)       # замість 0, 1, 2 підписуємо класи 1, 2, 3
plt.title('Кількість пасажирів за класом і статтю')
plt.xlabel('Клас каюти')
plt.ylabel('Кількість пасажирів')
plt.legend(title='Стать')
plt.show()

sns.countplot(data=df, x='Pclass', hue='Sex')
plt.title('Кількість пасажирів за класом і статтю')
plt.xlabel('Клас каюти')
plt.ylabel('Кількість пасажирів')
plt.legend(title='Стать')
plt.show()

x = np.linspace(-5, 5, 500)
y = -(x ** 3) - (6 * x) + 4
plt.plot(x, y)
plt.title('y = −x³ − 6x + 4')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x = np.linspace((-4 * np.pi), (4 * np.pi), 100)
y = np.cos((3 * x) - (np.pi / 4)) - (x * np.sin(x))
plt.plot(x, y)
plt.title('y = cos(3x − π/4) − x·sin x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

phi = np.linspace((-np.pi / 2), (np.pi / 2), 1000)
rho = 2 + np.cos(6 * phi)
ax = plt.subplot(projection='polar')
ax.plot(phi, rho)
ax.set_thetamin(-90)
ax.set_thetamax(90)
ax.set_title('ρ = 2 + cos 6φ')
plt.show()


