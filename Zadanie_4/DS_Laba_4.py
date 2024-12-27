import random
import datetime
from prettytable import PrettyTable
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum_of_digits(n))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_to_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_to_n(n - 1)
t = PrettyTable(['Номер элемента','sum_of_digits', 'digital_root', 'factorial', 'sum_to_n'])

for i in range(100):
    x = random.randint(1,1000)
    start1 = datetime.datetime.now()
    sum_of_digits(x)
    finish1 = datetime.datetime.now()

    start2 = datetime.datetime.now()
    digital_root(x)
    finish2 = datetime.datetime.now()

    start3 = datetime.datetime.now()
    factorial(x)
    finish3 = datetime.datetime.now()

    start4 = datetime.datetime.now()
    sum_to_n(x)
    finish4 = datetime.datetime.now()

    t.add_row([i+1, str(finish1 - start1), str(finish2 - start2), str(finish3 - start3), str(finish4 - start4)])
print(t)