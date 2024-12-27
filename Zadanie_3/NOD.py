import datetime
from prettytable import PrettyTable
import random
def NOD(N,M):
    arr=prosto(N)
    Max=0
    for i in range(len(arr)):
        if M%arr[i]==0 and arr[i]>Max:
            Max=arr[i]
    return Max
def NOD_Reverse(N,M):
    arr=prosto(N)
    Max=0
    for i in range(len(arr)-1,0,-1):
        if M%arr[i]==0 and arr[i]>Max:
            Max=arr[i]
    return Max
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return max(a, b)
def prosto(n):
    x=n
    arr=[]
    for i in range(1,n+1):
        if x%i==0:
            arr.append(i)
    return arr

x=0
y=10000
t = PrettyTable(['Число N','Число M','NOD от 1 до min(N,M)', 'NOD от min(N,M) до 1', 'Алгоритм Евклиада'])
for i in range(50):
    N = random.randint(x,y)
    M = random.randint(x,y)

    start1 = datetime.datetime.now()
    NOD(min(N,M), max(N,M))
    finish1 = datetime.datetime.now()

    start2 = datetime.datetime.now()
    NOD_Reverse(min(N,M), max(N,M))
    finish2 = datetime.datetime.now()

    start3 = datetime.datetime.now()
    gcd(min(N,M),max(N,M))
    finish3 = datetime.datetime.now()

    t.add_row([N,M,str(finish1 - start1) , str(finish2 - start2), str(finish3 - start3)])
    x+=1000
    y+=10000
print(t)