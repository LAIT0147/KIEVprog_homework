import module_human
import datetime


class Student(module_human.Human):
    """
    :param name;
    :param surname;
    :param date_of_birth: YYYY/MM/DD
    :param course;
    """
    def __init__(self, sex: str, nationality: str, name: str, surname: str, date_of_birth, course: int):
        super().__init__(sex, nationality)
        if not name or not surname or not date_of_birth or not course:
            raise ValueError('Some params are empty!')
        if not isinstance(name, str) and not isinstance(surname, str) and\
                not isinstance(date_of_birth, str) and not isinstance(course, int):
            raise TypeError('Invalid params')
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.course = course

    def __str__(self):
        age = datetime.datetime.now().year - datetime.date(*map(int, self.date_of_birth.split('/'))).year
        return super().__str__()+f'Name: {self.name}\nSurname: {self.surname}\n' \
                                 f'Age: {age} y.o.\nCourse: {self.course}\n'
