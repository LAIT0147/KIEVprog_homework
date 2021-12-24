class Human:
    def __init__(self, sex, nationality):
        self.sex = sex
        self.nationality = nationality

    def __str__(self):
        return f'Sex: {self.sex}\nNationality: {self.nationality}\n'


class Student(Human):
    def __init__(self, sex, nationality, name, surname, age, course):
        super().__init__(sex, nationality)
        self.name = name
        self.surname = surname
        self.age = age
        self.course = course

    def __str__(self):
        return super().__str__()+f'Name: {self.name}\nSurname: {self.surname}\n' \
                                 f'Age: {self.age} y.o.\nCourse: {self.course}\n'


class Group:
    def __init__(self, students):
        self.students = students

    def add(self, student):
        self.students.append(student)

    def search(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student

    def remove(self, surname):
        for student in self.students:
            if student.surname == surname:
                self.students.remove(student)

    def __str__(self):
        self.final_list = ""
        for i in range(len(self.students)):
            self.final_list += self.students[i].surname + " " + self.students[i].name[0] + "." + "\n"
        return self.final_list

kovalskii = Student('Man', "Ukr", "Bogdan", "Kovalskii", 19, 2)
didovec = Student('Man', "Ukr", "Vlad", "Didovec", 19, 2)
tokar = Student('Man', "Ukr", "Nikita", "Tokar", 19, 2)
andrienko = Student('Man', "Ukr", "Ilia", "Andrienko", 18, 2)
kaznadey = Student('Man', "Ukr", "Egor", "Kaznadey", 18, 2)
bril = Student('Woman', "Ukr", "Kate", "Bril", 19, 2)
malchenko = Student('Man', "Ukr", "Hlib", "Malchenko", 19, 2)
matkovskii = Student('Man', "Ukr", "Stas", "Matkovskii", 20, 2)
ivanov = Student('Man', "Ukr", "Ivan", "Ivanov", 18, 2)
kud = Student('Man', "Ukr", "Vlad", "Kud", 19, 2)

comp_engineering = [kovalskii, didovec, tokar, andrienko, kaznadey, bril, malchenko, matkovskii, ivanov]
KI_21 = Group(comp_engineering)
print("Group KI\n", KI_21)
print()

KI_21.add(kud)
print("Added new student (kud)\n", KI_21)

print("Searching for a student\n", KI_21.search("Kud"))

KI_21.remove("Ivanov")
print("Removed student(Ivanov)\n", KI_21)
