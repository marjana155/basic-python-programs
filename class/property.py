class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price can not be negative")
        else:
            self.__price = value
    #price = property(get_price, set_price)


product = Product(10)
#product.price = 100
print(product.price)
