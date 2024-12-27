import datetime
from prettytable import PrettyTable
import random
def prosto(n):
    x=n
    arr=[]
    for i in range(2,n):
        if x%i==0:
            arr.append(i)

    if len(arr)==0:
        return True
    else:
        return False
def prosto_2(n):
    x=n
    arr=[]
    if x%2==0:
        return False
    for i in range(3,n,2):
        if x%i==0:
            arr.append(i)

    if len(arr) == 0:
        return True
    else:
        return False
def prosto_sqrt(n):
    x=n
    arr=[]
    for i in range(2,int(n**0.5)+1):
        if x%i==0:
            arr.append(i)
            if x%(x//i)==0 and i!=(x//i):
                arr.append(x//i)

    if len(arr) == 0:
        return True
    else:
        return False
def prosto_sqrt_2(n):
    x=n
    arr=[]
    if x%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if x%i==0:
            arr.append(i)
            if x%(x//i)==0 and i!=(x//i):
                arr.append(x//i)

    if len(arr) == 0:
        return True
    else:
        return False

# Функция для форматирования timedelta
def format_time(delta):
    total_seconds = delta.total_seconds()
    micros = delta.microseconds
    return f"{int(total_seconds // 3600):02}:{int((total_seconds % 3600) // 60):02}:{int(total_seconds % 60):02}.{micros:15}"



x=0
y=100000
t = PrettyTable(['Число','Prosto', 'Prosto_2', 'Prosto_SQRT','Prosto_SQRT_2'])
for i in range(50):
    n=random.randint(x,y)
    start1 = datetime.datetime.now()
    prosto(n)
    finish1 = datetime.datetime.now()

    start2 = datetime.datetime.now()
    prosto_2(n)
    finish2 = datetime.datetime.now()

    start3 = datetime.datetime.now()
    prosto_sqrt(n)
    finish3 = datetime.datetime.now()

    start4 = datetime.datetime.now()
    prosto_sqrt_2(n)
    finish4 = datetime.datetime.now()

    t.add_row([n,format_time(finish1 - start1) , format_time(finish2 - start2), format_time(finish3 - start3),format_time(finish4 - start4)])
    x=y
    y+=10000
print(t)