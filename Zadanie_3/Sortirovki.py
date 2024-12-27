import random
import datetime
from prettytable import PrettyTable


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr
def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr

t = PrettyTable(['Номер массива','Сортировка выборкой', 'Пузырьковая сортировка', 'Встроенная сортировка'])
for g in range(10):
    arr = []
    for i in range(100):
        arr.append(random.randint(1,10000))
    start1 = datetime.datetime.now()
    arr1=arr
    selection_sort(arr1)
    finish1 = datetime.datetime.now()

    start2 = datetime.datetime.now()
    arr2=arr
    bubble_sort(arr2)
    finish2 = datetime.datetime.now()

    start3 = datetime.datetime.now()
    sorted(arr)
    finish3 = datetime.datetime.now()

    t.add_row([g+1, str(finish1 - start1), str(finish2 - start2), str(finish3 - start3)])
print(t)
