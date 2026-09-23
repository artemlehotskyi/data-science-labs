import numpy as np
np.random.seed(42)

k = np.arange(0,101)
total = np.sum(1 / (1 + np.exp(-(k-2) ** 2)))
print(total)


