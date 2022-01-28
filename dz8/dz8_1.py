def func(a):
    x = 2
    return a**x


def func_gen(b, n):
    i = 0
    while i < n:
        yield func(b)
        b = b + 3


f = func_gen(5, 8)
for i in f:
    if i > 500:
        f.close()
        break
    print(i)