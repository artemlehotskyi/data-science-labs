import numpy as np

np.random.seed(69)


arr_a = np.random.randint(1, 11, 5)

result = arr_a @ arr_a

print(result)


# 2D

arr_2d = np.reshape(arr_a, (-1, 1))

result_2d = np.transpose(arr_2d) @ arr_2d

print(result_2d.shape)
print(result_2d.item())
