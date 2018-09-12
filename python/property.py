class FriedChicken:
    def __init__(self):
        self._price = 0

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    price = property(get_price, set_price)


class FriedChickenWithDecorator:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('price is more than 0')

        self._price = value
        if value > 100000:
            self._price -= value * 0.1


class A:
    @property
    def new1(self):
        return self._new1

    @new1.setter
    def new1(self, value):
        self._new1 = value

if __name__ == '__main__':
    f1 = FriedChicken()
    f1.price = 2000
    print(f1.price)

    f2 = FriedChickenWithDecorator()
    f2.price = 1500000
    print(f2.price)
