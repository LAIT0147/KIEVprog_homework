import random


def lst_sum(n):
    summa = 0
    for items in n:
        if isinstance(items, int or float):
            summa = summa + items
        else:
            raise TypeError()
    return summa


lst = []
[lst.append(random.randint(1, 100)) for i in range(10)]
print(lst)
print(lst_sum(lst))
