import time
from prettytable import PrettyTable
from math import isqrt

# Метод полного перебора для дискретного логарифмирования
def brute_force_discrete_log(base, result, mod):
    count = 0
    exp = 0
    current = 1
    while current != result:
        current = (current * base) % mod
        exp += 1
        count += 1
        if exp >= mod:  # Если перебрали все возможные значения, выходим из цикла
            return None, count
    return exp, count

# Метод "Шаг младенца – шаг великана" (метод Шэнкса)
def baby_step_giant_step(base, result, mod):
    n = int(isqrt(mod)) + 1
    count = 0

    # Шаг младенца
    baby_steps = {pow(base, i, mod): i for i in range(n)}
    count += n

    # Шаг великана
    c = pow(base, n * (mod - 2), mod)  # c = base^(-n) mod mod
    for j in range(n):
        count += 1
        y = (result * pow(c, j, mod)) % mod
        if y in baby_steps:
            return j * n + baby_steps[y], count

    return None, count  # Если решение не найдено

# Функция для замера времени выполнения и количества умножений
def measure_performance(base, result, mod, method):
    start_time = time.time()
    exp, count = method(base, result, mod)
    end_time = time.time()
    return exp, count, (end_time - start_time) * 1000  # Время в миллисекундах

# Таблица для метода полного перебора
brute_force_table = PrettyTable()
brute_force_table.field_names = ["Base", "Result", "Modulus", "Exponent", "Multiplications", "Time (ms)"]

# Таблица для метода "Шаг младенца – шаг великана"
baby_giant_table = PrettyTable()
baby_giant_table.field_names = ["Base", "Result", "Modulus", "Exponent", "Multiplications", "Time (ms)"]

# Примеры данных для тестирования
test_data = [
    (2, 22, 104729),
    (3, 13, 104729),
    (5, 18, 104729),
    (7, 21, 104729),
    (11, 33, 104729),
]

# Заполнение таблиц
for base, result, mod in test_data:
    exp, count, time_taken = measure_performance(base, result, mod, brute_force_discrete_log)
    brute_force_table.add_row([base, result, mod, exp, count, f"{time_taken:.9f}"])

    exp, count, time_taken = measure_performance(base, result, mod, baby_step_giant_step)
    baby_giant_table.add_row([base, result, mod, exp, count, f"{time_taken:.9f}"])

# Вывод таблиц
print("Метод полного перебора:")
print(brute_force_table)

print("\nМетод 'Шаг младенца – шаг великана':")
print(baby_giant_table)
