from datetime import datetime
import time


def memoization(func):
    mem = dict()

    def mem_func(*arg):
        if arg in mem:
            print('Value in cache')
            return mem[arg]
        else:
            value = func(*arg)
            mem[arg] = value
            print(mem)
            return value
    return mem_func


def fibonachi(n):
    first_num = 0
    second_num = 1
    i = 1
    while i <= n:
        next_num = first_num + second_num
        first_num = second_num
        second_num = next_num
        i = i + 1
        yield next_num


mem_fibonachi = memoization(fibonachi)
m = mem_fibonachi(200)
start_time = datetime.now()
for i in m:
    print(i)
print(datetime.now() - start_time)
second_time = datetime.now()
p = fibonachi(200)
for item in p:
    print(item)
print(datetime.now() - second_time)
