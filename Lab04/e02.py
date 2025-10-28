class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell_all(self):
        return self.quantity * self.price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def describe(self):
        print("Name: {}, Price: {}, Quantity: {}, Total: {}".format(self.name, self.price, self.quantity, self.sell_all()))


banana = Product("Banana", 10, 100)
print(banana.describe())

banana.update_quantity(5)
print(banana.describe())