import module_students
MAX_STUDENTS = 10


class Group:
    def __init__(self, students=None):
        self.__students = []
        for item in students:
            self.add(item)

    def add(self, student: module_students.Student):
        if len(self.__students) >= MAX_STUDENTS:
            raise TypeError('Too many students in one group!')
        for item in self.__students:
            if (item.name, item.surname, item.date_of_birth) == (student.name, student.surname, student.date_of_birth):
                raise TypeError('We already have that student')
        self.__students.append(student)

    def search(self, surname):
        if not isinstance(surname, str):
            raise TypeError('Invalid params!')
        for student in self.__students:
            if student.surname == surname:
                return student

    def remove(self, surname):
        if not isinstance(surname, str):
            raise TypeError('Invalid params!')
        for student in self.__students:
            if student.surname == surname:
                self.__students.remove(student)

    def __str__(self):
        res = '\n'.join(map(str, self.__students))
        return f'Students:\n{res}'

