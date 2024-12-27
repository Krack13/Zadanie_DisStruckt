def power(a, b):
    if b == 0:
        return 1  # Базовый случай: любое число в степени 0 равно 1
    else:
        return a * power(a, b - 1)  # Рекурсивный шаг: a * a^(b-1)

def gcd(a, b):
    if b == 0:
        return a  # Базовый случай: НОД найден
    else:
        return gcd(b, a % b)  # Рекурсивный шаг: вызываем gcd для (b, a % b)

# Пример вызова gcd
print(gcd(48, 18))  # Результат: 6
print(gcd(1071, 462))  # Результат: 21
print(gcd(56, 98))  # Результат: 14
# Пример вызова power
print(power(2, 3))  # Результат: 8 (2^3)
print(power(5, 0))  # Результат: 1 (5^0)
print(power(3, 4))  # Результат: 81 (3^4)

