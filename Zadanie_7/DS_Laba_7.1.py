import time
from prettytable import PrettyTable

# Наивный метод возведения в степень по модулю
def naive_mod_exp(base, exp, mod):
    result = 1
    count = 0
    for _ in range(exp):
        result = (result * base) % mod
        count += 1
    return result, count

# Алгоритм быстрого возведения в степень по модулю
def fast_mod_exp(base, exp, mod):
    result = 1
    count = 0
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
            count += 1
        exp = exp >> 1
        base = (base * base) % mod
        count += 1
    return result, count

# Функция для замера времени выполнения и количества умножений
def measure_performance(base, exp, mod, method):
    start_time = time.time()
    result, count = method(base, exp, mod)
    end_time = time.time()
    return result, count, end_time - start_time

# Таблица для наивного метода
naive_table = PrettyTable()
naive_table.field_names = ["Base", "Exponent", "Modulus", "Result", "Multiplications", "Time (s)"]

# Таблица для быстрого метода
fast_table = PrettyTable()
fast_table.field_names = ["Base", "Exponent", "Modulus", "Result", "Multiplications", "Time (s)"]

# Примеры данных для тестирования
test_data = [
    (248949, 14980, 12347),
    (348498, 24480, 12358),
    (48944, 34880, 87984),
    (487998, 49877, 465),
    (789654, 58897, 184900),
]

# Заполнение таблиц
for base, exp, mod in test_data:
    result, count, time_taken = measure_performance(base, exp, mod, naive_mod_exp)
    naive_table.add_row([base, exp, mod, result, count, time_taken])

    result, count, time_taken = measure_performance(base, exp, mod, fast_mod_exp)
    fast_table.add_row([base, exp, mod, result, count, time_taken])

# Вывод таблиц
print("Наивный метод:")
print(naive_table)

print("\nАлгоритм быстрого возведения в степень:")
print(fast_table)
