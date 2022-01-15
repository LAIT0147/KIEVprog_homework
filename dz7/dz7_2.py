"""
Реализуйте свой аналог генераторной функции range(). Да, вы теперь
знаете, что это - генератор.
"""
def funcrange(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1

f = funcrange(10)
for i in f:
    print(i)
