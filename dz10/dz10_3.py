"""
Для класса Box напишите статический метод, который будет подсчитывать
суммарный объем двух ящиков, которые будут его параметрами.
"""


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = " + str(self.x)+", y = " + str(self.y) + ", z = " + str(self.z) + " ]"

    def get_v(self):
        return self.x * self.y * self.z

    @staticmethod
    def summa_v(a, b):
        return Box.get_v(a) + Box.get_v(b)


x = Box(5, 6, 7)
y = Box(7, 8, 9)

print(Box.summa_v(x, y))
