import math

def cos_x(x: float, eps: float) -> float:
    if eps <= 0:
        raise ValueError("eps cannot be negative or zero")
    current = 1
    total = 0
    k = 0
    while abs(current) > eps:
        total += current
        current = current * (-(x ** 2) / ((2 * k + 1) * (2 * k + 2)))
        k += 1
    return total

# Tests
eps = 1e-6
tests = [0, 1, -2, 3.14]

for numm in tests:
    approx = cos_x(numm, eps)
    exact = math.cos(numm)
    print(f"x = {numm}:\ncos_x = {approx:.8f}, math.cos = {exact:.8f}\n")
