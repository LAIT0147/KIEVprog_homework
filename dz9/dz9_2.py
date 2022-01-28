"""
Создайте декоратор, который зарегистрирует декорируемую функцию в
списке функций, для обработки последовательности.
"""
function_list = []


def to_list(f):
    function_list.append(f)
    return f


@to_list
def plus(a, b):
    return a + b


@to_list
def minus(a, b):
    return a - b


a = plus(4, 6)
b = minus(5, 1)
print(a)
print(b)
print(function_list)
