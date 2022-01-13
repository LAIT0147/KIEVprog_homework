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

    def __iter__(self):
        return GroupIterator(self.__students)


class GroupIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.wrapped):
            self.i += 1
            return self.wrapped[self.i - 1]
        raise StopIteration()
