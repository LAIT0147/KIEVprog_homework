import abc
"""
Создайте ABC класс с абстрактным методом проверки целого числа на
простоту. Т.е., если параметром этого метода является целое число и оно
простое, то метод должен вернуть True, а в противном случае False.

Создайте класс его наследующий.

Создайте класс, который не наследует пользовательский ABC класс, но
обладает нужным методом. Зарегистрируйте его в качестве виртуального
подкласса.
"""


class Check(abc.ABC):
    def __init__(self, a):
        self.a = a

    @abc.abstractmethod
    def get_number(self):
        pass

    @classmethod
    def __subclasshook__(abc_class, cls):
        for sub_class in cls.__mro__:
            for property_name in sub_class.__dict__:
                if property_name == "get_number":
                    return True
        return False


class TrueCheck(Check):
    def __init__(self, a):
        super().__init__(a)

    def get_number(self):
        return f'Number {self.a} is True'


class FalseCheck:
    def __init__(self, x: int):
        self.x = x

    def get_number(self):
        return f'Number {self.x} is False'


def make_number(x):
    k = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            k = k + 1
    if k <= 0:
        return TrueCheck(x)
    else:
        return FalseCheck(x)


if __name__ == "__main__":
    b = make_number(47)
    c = make_number(49)
    print(b.get_number())
    print(c.get_number())
    print(isinstance(b, Check))
    print(isinstance(c, Check))
