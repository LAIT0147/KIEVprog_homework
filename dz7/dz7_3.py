"""
Напишите функцию-генератор, которая будет возвращать простые числа.
Верхняя граница этого диапазона должна быть задана параметром этой
функции.
"""
def easynum (n):

    for num in range(2, n):
        prime = True
        for item in range(2, num):
            if num % item == 0:
                prime = False
        if prime:
            yield num
    return

f = easynum(20)
for i in f:
    print(i)
