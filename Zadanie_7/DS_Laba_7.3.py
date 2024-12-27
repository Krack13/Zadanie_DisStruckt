import time
from prettytable import PrettyTable
from sympy import isprime, nextprime

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

# Функция для вычисления общего секретного ключа по системе Диффи-Хеллмана
def diffie_hellman(p, g, a, b):
    # Алиса вычисляет A
    A, count_a = fast_mod_exp(g, a, p)
    # Боб вычисляет B
    B, count_b = fast_mod_exp(g, b, p)

    # Алиса вычисляет общий секретный ключ
    S_alice, count_alice = fast_mod_exp(B, a, p)
    # Боб вычисляет общий секретный ключ
    S_bob, count_bob = fast_mod_exp(A, b, p)

    return A, B, S_alice, S_bob, count_a + count_b + count_alice + count_bob

# Таблица для результатов
dh_table = PrettyTable()
dh_table.field_names = ["p", "g", "a", "b", "A", "B", "S_alice", "S_bob", "Multiplications", "Time (ms)"]

# Генерация больших простых чисел
p = nextprime(10**500)  # Очень большое простое число
g = 2  # Основание

# Примеры данных для тестирования
test_data = [
    (p, g, 1234567890123456789012345678901234567890, 987654321098765432109876543210987654321),
    (p, g, 2345678901234567890123456789012345678901, 876543210987654321098765432109876543210),
    (p, g, 3456789012345678901234567890123456789012, 765432109876543210987654321098765432109),
    (p, g, 4567890123456789012345678901234567890123, 654321098765432109876543210987654321098),
    (p, g, 5678901234567890123456789012345678901234, 543210987654321098765432109876543210987),
]

# Заполнение таблицы
for p, g, a, b in test_data:
    start_time = time.time()
    A, B, S_alice, S_bob, count = diffie_hellman(p, g, a, b)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000  # Время в миллисекундах
    dh_table.add_row([p, g, a, b, A, B, S_alice, S_bob, count, f"{time_taken:.9f}"])

# Вывод таблицы
print("Результаты вычисления общего секретного ключа по системе Диффи-Хеллмана:")
print(dh_table)
