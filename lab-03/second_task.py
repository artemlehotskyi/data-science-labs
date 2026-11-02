import numpy as np

A = np.array([

    [6, -1, 5],
    [2, 2, -5],
    [3, 7, -2]
])
b = np.array([4, -3, 5])

det_A = np.linalg.det(A)


if np.allclose(det_A, 0):
    print("det(A) = 0 → система не має єдиного розв'язку")
else:
    print("det(A) ≠ 0 → система має єдиний розв'язок")

print(f"det(A) = {det_A}")
x = np.linalg.solve(A, b)

A1 = np.copy(A)
A1[:, 0] = b
det1 = np.linalg.det(A1)

x_1 = det1 / det_A

A2 = np.copy(A)
A2[:, 1] = b

det2 = np.linalg.det(A2)

x_2 = det2 / det_A

A3 = np.copy(A)
A3[:, 2] = b

det3 = np.linalg.det(A3)

x_3 = det3 / det_A
