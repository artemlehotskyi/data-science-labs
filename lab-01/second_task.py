import random

random.seed(42)

def max_abs(lst: list[float]) -> float:
    if len(lst) == 0:
        raise ValueError("List is empty")
    current_max = 0
    for num in lst:
        abs_num = abs(num)
        if abs_num > current_max:
            current_max = abs_num
    return current_max

lst1 = [3, -7, 2]
lst2 = [random.randint(-10, 10) for _ in range(10)]

print(f"Список: {lst1}, max_abs = {max_abs(lst1)}")
print(f"Список: {lst2}, max_abs = {max_abs(lst2)}")
