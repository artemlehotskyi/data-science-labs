from collections.abc import Callable

def f(a: float) -> float:
    return 5 * a ** 6 + 3 * a ** 2 - 10


def df(a: float) -> float:
    return 30 * a ** 5 + 6 * a

a0 = 1
alpha = 0.01

def gradient_descent(
    f: Callable[[float], float],
    df: Callable[[float], float],
    a0: float,
    alpha: float,
    epsilon: float = 1e-7,
    max_iter: int = 10_000,
) -> tuple[float, float, int] | None:
    n = 0
    try:
        while True:
            a = a0 - alpha * df(a0)
            n += 1
            if abs(a - a0) <= epsilon or n >= max_iter:
                break
            a0 = a
    except OverflowError:
        return None
    return a, f(a), n


for a0, alpha in [(a0, alpha), (a0, 0.1), (2, alpha)]:
    result = gradient_descent(f, df, a0, alpha)
    print(f"a0 = {a0}, alpha = {alpha}")
    if result is None:
        print("  спуск розбігся (OverflowError)")
    else:
        a, fa, n = result
        print(f"  a = {a:.6f}")
        print(f"  f(a) = {fa:.6f}")
        print(f"  n = {n}")

