import numpy as np
np.random.seed(42)

arr = np.random.randint(-4,14, size=10)

result = np.where(arr % 2 == 0, 0, arr)
print(result)
