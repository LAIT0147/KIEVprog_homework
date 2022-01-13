# Создайте класс «Прямоугольник», у которого присутствуют два поля
# (ширина и высота). Реализуйте метод сравнения прямоугольников по
# площади. Также реализуйте методы сложения прямоугольников (площадь
# суммарного прямоугольника должна быть равна сумме площадей
# прямоугольников, которые вы складываете). Реализуйте методы
# умножения прямоугольника на число n (это должно увеличить площадь
# базового прямоугольника в n раз).

class Rectangle:

    def __init__(self, width, height):
        if not width or not height:
            raise ValueError('Some params are empty!')
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle:\nWidth x Height: {self.width}x{self.height}'

    def __mul__(self, other):
        return Rectangle(self.width * other, self.height * other)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        if isinstance(other, tuple):
            width, height = other
            return Rectangle(self.width + width, self.height + height)

    def __get_s(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.__get_s() == other.__get_s()

    def __ne__(self, other):
        return self.__get_s() != other.__get_s()


x = Rectangle(4, 5)
y = Rectangle(5, 9)
z = x * 2
print(x)
print(y)
print(z)
print(x + y)
print(x == y)
