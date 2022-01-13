from math import gcd
# Создайте класс «Правильная дробь» и реализуйте методы сравнения,
# сложения, вычитания и произведения для экземпляров этого класса.


class RightFraction:

    def __init__(self, a, b):
        if not a or not b:
            raise ValueError('Some params are empty!')
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('Params must be integer')
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} / {self.b}'

    def __add__(self, other):
        if self.b != other.b:
            new_a = self.a * other.b + self.b * other.a
            new_b = self.b * other.b
        else:
            new_a = self.a + other.a
            new_b = self.b
        f = int(gcd(new_a, new_b))
        return RightFraction(new_a//f, new_b//f)

    def __sub__(self, other):
        if self.b != other.b:
            new_a = self.a * other.b - self.b * other.a
            new_b = self.b * other.b
        else:
            new_a = self.a - other.a
            new_b = self.b
        f = int(gcd(new_a, new_b))
        return RightFraction(new_a//f, new_b//f)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return self.a != other.a or self.b != other.b


x = RightFraction(2, 4)
y = RightFraction(1, 4)
z = x + y
print(z)
print(x == y)