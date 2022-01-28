"""
Создайте дескриптор, который будет делать поля класса управляемые им
доступными только для чтения.
"""


class Descriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        raise AttributeError('Read only!')


class Field:
    def __init__(self, name):
        self.name = name

    field_greetings = Descriptor('Hello my dear friend.')

    def __str__(self):
        return f'{self.field_greetings}\nMy name is {self.name}'


a = Field('Vlad')
print(a.field_greetings)
print(a)
