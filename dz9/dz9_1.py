
"""
Создайте декоратор, который будет подсчитывать, сколько раз была
вызвана декорируемая функция.
"""


def to_str(func):
    count = 0

    def inner_func(*args):
        nonlocal count
        count += 1
        return str(func(*args)), count
    return inner_func


@to_str
def function(x, a):
    return x**a


a = function(4, 2)
b = function(5, 3)
print(a)
print(b)