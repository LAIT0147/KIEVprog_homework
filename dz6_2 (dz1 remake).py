MIN_PRICE = 0


class Order:
    def __init__(self, surname: str, name: str, phone_number: int):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.check = 0
        self.order = []
        if not surname or not name or not phone_number:
            raise ValueError('Some params are empty!')
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(phone_number, int):
            raise TypeError('Invalid params')

    def buy(self, good: str, price: float):
        """
        You must write price like this 99.00
        :param good:
        :param price: float
        """
        if not good or not price:
            raise ValueError('Param is empty')
        if not isinstance(good, str):
            raise TypeError('Invalid param')
        if not isinstance(price, float):
            raise ValueError('Invalid param')
        # if not isinstance(price, float or int):
            # raise ValueError('Invalid param')
        if price < MIN_PRICE:
            raise ValueError('Invalid param')
        self.order.append(good)
        self.check += price

    def __str__(self):
        return f'Shopping basket:\nProducts: {", ".join(self.order)}\n' \
               f'Customer data:\n{self.surname}\t{self.name}\n{self.phone_number}\n' \
               f'The final price: {self.check}'

    def __iter__(self):
        return OrderIterator(self.order)


class OrderIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.i = 0

    def __next__(self):
        if self.i < len(self.wrapped):
            self.i += 1
            return self.wrapped[self.i - 1]
        raise StopIteration()


buyer_1 = Order("Ivanov", "Ivan", 2525612)
buyer_1.buy("Pen", 22.0)
buyer_1.buy("Pencil", 61.8)
for i in buyer_1:
    print(i)
