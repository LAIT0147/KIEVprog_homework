"""
Реализуйте функционал, который будет запрещать установку полей класса
любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
попытаться присвоить, например, строку, то должно быть возбужденно
исключение.

"""


class Conference:
    def __init__(self, theme, numb_of_people):
        self.theme = theme
        self.__numb_of_people = numb_of_people

    @property
    def number_of_persons(self):
        return f'{self.__numb_of_people} people will be at the conference'

    @number_of_persons.setter
    def number_of_persons(self, value):
        if not isinstance(value, int):
            raise TypeError('Param is wrong!')
        if value < 3:
            raise ValueError('Conference cant have this number of people!')

        self.__numb_of_people = value

    @number_of_persons.deleter
    def number_of_persons(self):
        pass

    def __str__(self):
        res = ''
        for key, value in self.__dict__.items():
            res += f'{key} : {value}\n'
        return res


a = Conference('Science', 18)
print(a)
a.number_of_persons = 20
print(a)
print(a.number_of_persons)
a.number_of_persons = 'setasfa'