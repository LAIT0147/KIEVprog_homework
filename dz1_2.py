class Customer:
    """
    Создайте класс «Покупатель». В качестве полей можете
    использовать фамилию, имя, отчество, мобильный телефон и т. д.
    """
    def __init__(self, surname, name, middle_name, phone_number):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.middle_name[0]}.\n{self.phone_number}'


cus_1 = Customer("Karpenko", "Egor", "Stanislavovish", 23456789)
cus_2 = Customer("Rybalko", "Vitalii", "Nikolaevish", 9876543)
print(cus_1)
print()
print(cus_2)
