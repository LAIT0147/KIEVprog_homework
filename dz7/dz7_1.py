"""
Реализуйте генераторную функцию, которая будет возвращать по
одному члену геометрической прогрессии с указанным множителем.
Генератор должен остановить свою работу или по достижению указанной
границы, или при передаче команды на завершение.
"""
# bn = b1 * q^(n-1)
def geoprog (b, q):
    n = 1
    while n < 10:
        yield b * q**(n-1)
        b = b * q**(n-1)
        n = n + 1
    return

f = geoprog(5, 2)
for i in f:
    if i > 300:
        f.close()
        break
    print(i)