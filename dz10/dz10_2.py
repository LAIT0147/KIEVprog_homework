"""
Создайте декоратор класса с параметром. Параметром должна быть
строка, которая должна дописываться (слева) к результату работы метода
__str__.
"""


class DecoratorClass:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        new_instance = self.cls(*args, **kwargs)
        self.param = str('Student')
        return new_instance


@DecoratorClass
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{Student.param} Name: {self.name}\tSurname: {self.surname}\t'


x = Student("Vlad", 'Kud')
y = Student("Egor", "Egorovich")
print(x)
print(y)
