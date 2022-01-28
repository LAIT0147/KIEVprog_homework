from  datetime import datetime
"""
Реализуйте свойство класса, которое обладает следующим
функционалом: при установки значения этого свойства в файл с заранее
определенным названием должно сохранятся время (когда устанавливали
значение свойства) и установленное значение.
"""


class Writer:
    def __init__(self, budget):
        self.__budget = budget

    @property
    def budget(self):
        return f'The current budget of the company is {self.__budget}$'

    @budget.setter
    def budget(self, value):
        if not isinstance(value, int):
            raise TypeError('Param is wrong!')
        if value < 300:
            raise ValueError('We are not soo much poor!')
        d = datetime.now()
        a = f'Changed value from {self.__budget}$ to {value}$ by {d}'
        with open('dz11_3.txt', 'a') as f:
            f.write(a + '\n')
            f.close()
        self.__budget = value

    @budget.deleter
    def budget(self):
        pass

    def __str__(self):
        return f'Current budget is {self.__budget}'


x = Writer(3000)
print(x)
x.budget = 10000
print(x)
