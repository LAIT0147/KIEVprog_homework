"""
Напишите выражение-генератор для заполнения списка. Список должен
быть заполнен кубами чисел от 2 и до указанной вами величины.
"""


def lst(n):
    a = []
    i = 2
    x = 2
    while i <= n:
        a.append(i**x)
        i = i + 1
    yield a
    return


f = lst(10)
for i in f:
    print(i)