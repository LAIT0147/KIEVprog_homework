class Goods:
    """
    Создайте пользовательский класс для описания товара
    (предположим, это задел для интернет-магазина). В качестве
    полей товара можете использовать значение цены, описание,
    габариты товара. Создайте пару экземпляров вашего класса и
    протестируйте их работу.
    """
    def __init__(self, name, price, dimensions, description):
        self.name = name
        self.price = price
        self.dimensions = dimensions
        self.description = description

    def __str__(self):
        return f'Name = {self.name}\nPrice = {self.price}$\nDimensions = {self.dimensions}' \
               f'\nDescription = {self.description}'


item_1 = Goods("Pen", 1, "width 10sm, diameter 1,3 sm", "Good pen for work or drawing")
item_2 = Goods('Notebook', 0.5, "40x50sm, 96 pages", "Very good paper and cool design")

print(item_1)
print()
print(item_2)

