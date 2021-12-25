import datetime

MAX_STUDENTS = 10


class Human:
    def __init__(self, sex: str, nationality: str):
        self.sex = sex
        self.nationality = nationality
        if not sex or not nationality:
            raise ValueError('Some params are empty!')
        if not isinstance(sex, str) and not isinstance(nationality, str):
            raise TypeError('Invalid params')

    def __str__(self):
        return f'Sex: {self.sex}\nNationality: {self.nationality}\n'


class Student(Human):
    """
    :param name;
    :param surname;
    :param date_of_birth: YYYY/MM/DD
    :param course;
    """
    def __init__(self, sex: str, nationality: str, name: str, surname: str, date_of_birth, course: int):
        super().__init__(sex, nationality)
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.course = course
        if not name or not surname or not date_of_birth or not course:
            raise ValueError('Some params are empty!')
        if not isinstance(name, str) and not isinstance(surname, str) and\
                not isinstance(date_of_birth, str) and not isinstance(course, int):
            raise TypeError('Invalid params')

    def __str__(self):
        age = datetime.datetime.now().year - datetime.date(*map(int, self.date_of_birth.split('/'))).year
        return super().__str__()+f'Name: {self.name}\nSurname: {self.surname}\n' \
                                 f'Age: {age} y.o.\nCourse: {self.course}\n'


class Group:
    def __init__(self, students=None):
        self.__students = []
        for item in students:
            self.add(item)

    def add(self, student: Student):
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
            else:
                print('There are no student that you searching.')

    def remove(self, surname):
        if not isinstance(surname, str):
            raise TypeError('Invalid params!')
        for student in self.__students:
            if student.surname == surname:
                self.__students.remove(student)
            else:
                print('There are no student named', surname)

    def __str__(self):
        res = '\n'.join(map(str, self.__students))
        return f'Students:\n{res}'


kovalskii = Student('Man', "Ukr", "Bogdan", "Kovalskii", '2000/12/12', 2)
didovec = Student('Man', "Ukr", "Vlad", "Didovec", '2002/4/19', 2)
tokar = Student('Man', "Ukr", "Nikita", "Tokar", '2002/9/13', 2)
andrienko = Student('Man', "Ukr", "Ilia", "Andrienko", '2001/1/25', 2)
kaznadey = Student('Man', "Ukr", "Egor", "Kaznadey", '2001/4/16', 2)
kud = Student('Man', "Ukr", "Vlad", "Kud", '2002/1/19', 2)


KI_21 = Group([kovalskii, didovec, tokar, andrienko, kaznadey])
print("Group KI\n", KI_21)
print()

KI_21.add(kud)
print("Added new student (kud)\n", KI_21)

print("Searching for a student\n", KI_21.search("Kud"))

KI_21.remove("Kaznadey")
print("Removed student(Kaznadey)\n", KI_21)
