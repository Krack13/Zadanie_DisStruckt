def print_1_to_n(n):
    if n > 0:
        print_1_to_n(n - 1)  # Рекурсивный вызов с уменьшением n
        print(n)  # Печатаем текущее значение после рекурсивного вызова

def print_n_to_1(n):
    if n > 0:
        print(n)  # Печатаем текущее значение
        print_n_to_1(n - 1)  # Рекурсивный вызов с уменьшением n

def print_neg_n_to_n(n, current=-1):
    if current <= n:
        print(current)  # Печатаем текущее значение
        print_neg_n_to_n(n, current + 1)  # Рекурсивный вызов, увеличиваем текущее значение

def print_n_to_neg_n(n):
    if n >= -n:
        print(n)  # Печатаем текущее значение
        print_n_to_neg_n(n - 1)  # Рекурсивный вызов с уменьшением n

def print_n_to_neg_n_mod2(n):
    if n>=-n:
        if n%2!=0:
            print(n)
        print_n_to_neg_n_mod2(n-1)
def even_numbers(n, current=None):
    if current is None:
        current = -n
    if current > n:
        return
    if current % 2 == 0:
        print(current)
    even_numbers(n, current + 1)

print(even_numbers(5))  # Пример вызова для n=5
"""# Пример вызова
print_n_to_neg_n(3)  # Результат: 3 2 1 0 -1 -...
# Пример вызова
print_neg_n_to_n(3)  # Результат: -1 0 1 2 3
# Пример вызова
print_n_to_1(5)  # Результат: 5 4 3 2 1
# Пример вызова
print_1_to_n(5)  # Результат: 1 2 3 4 5
"""
print(print_n_to_neg_n_mod2(10))