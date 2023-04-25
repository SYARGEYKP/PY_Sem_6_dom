# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)
from random import randint
a = [randint(1, 15) for i in range(20)]
print(a)
maxim = int(input('введите максимальное число '))
minim = int(input('введите минимальное число '))
for i in range(len(a)):
    if minim <= a[i] <= maxim:
        print(i, end=' ')


