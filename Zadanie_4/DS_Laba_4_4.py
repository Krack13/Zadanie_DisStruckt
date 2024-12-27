from functools import lru_cache
import random
import datetime
from prettytable import PrettyTable
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@lru_cache(None)  # Кешируем все вызовы функции
def fibonacci_memoized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

def fibonacci_array(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)  # Создаём массив длиной n+1
    fib[1] = 1  # Первые два числа Фибоначчи

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]  # Вычисляем и сохраняем в массив

    return fib[n]

def fibonacci_optimized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1  # Начальные значения F(0) и F(1)

    for _ in range(2, n + 1):
        a, b = b, a + b  # Сдвигаем значения: a = F(n-1), b = F(n)

    return b


t = PrettyTable(['Номер элемента', 'С кеш-памятью', 'С временным массивом', 'С вычислением на ленту'])

for i in range(1):
    x = 200

    #start1 = datetime.datetime.now()
    #fibonacci_recursive(x)
    #finish1 = datetime.datetime.now()

    start2 = datetime.datetime.now()
    fibonacci_memoized(x)
    finish2 = datetime.datetime.now()

    start3 = datetime.datetime.now()
    fibonacci_array(x)
    finish3 = datetime.datetime.now()

    start4 = datetime.datetime.now()
    fibonacci_optimized(x)
    finish4 = datetime.datetime.now()

    t.add_row([i+1, str(finish2 - start2), str(finish3 - start3), str(finish4 - start4)])
print(t)
print(fibonacci_memoized(x))
print(fibonacci_optimized(x))
print(fibonacci_array(x))