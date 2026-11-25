import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

def f(a):
    return (5 * a ** 6) + (3 * a ** 2) - 10

def df(a):
    return (30 * a ** 5) + (6 * a)

a0 = 1
alpha = 0.01
epsilon = 1e-7
max_iter = 10000
n = 0

while True:
    a = a0 - alpha * df(a0)
    n += 1
    if abs(a - a0) <= epsilon:
        break
    elif n >= max_iter:
        break
    else:
        a0 = a

print(f'a = {a:.6f}\n'
      f'f(a) = {f(a):.6f}\n'
      f'n = {n}')