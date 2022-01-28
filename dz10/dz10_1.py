"""
Создайте декоратор, который зарегистрирует декорируемый класс в
списке классов.
"""
class_list = []


def to_list(cls):
    class_list.append(cls)
    return cls


@to_list
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Students:\nName:{self.name}\tSurname:{self.surname}'


@to_list
class Teacher:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Teachers:\nName:{self.name}\tSurname:{self.surname}'


x = Student('Vlad', 'Kud')
y = Student('Ilia', 'Andr')
a = Teacher('Iryna', 'Tcach')
b = Teacher('Ludmyla', 'Basishina')

print(class_list)
