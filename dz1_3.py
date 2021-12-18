class Order:
    """
    Создайте класс «Заказ». Заказ может содержать несколько
    товаров. Заказ должен содержать данные о пользователе, который
    его осуществил. Реализуйте метод вычисления суммарной
    стоимости заказа. Определите метод __str__() для корректного
    вывода информации о этом заказе.
    """
    def __init__(self, surname, name, phone_number):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.check = 0
        self.order = []

    def buy(self, good, price):
        self.order.append(good)
        self.check += price

    def __str__(self):
        return f'Shopping basket:\nProducts: {", ".join(self.order)}\n' \
               f'Customer data:\n{self.surname}\t{self.name}\n{self.phone_number}\n' \
               f'The final price: {self.check}'


x = str(input("What is your surname?\t"))
y = str(input('Name?\t'))
z = int(input('And enter your phone number.(In one row without dashes)\t'))
buyer_1 = Order(x, y, z)
flag = True
while flag:
    a = str(input('Type name of product\t'))
    b = float(input('What is the price of this product?\t'))
    buyer_1.buy(a, b)
    c = str(input('Do you want to add more?\t'))
    if c.lower() == 'yes':
        continue
    else:
        flag = False
print()
print(buyer_1)
