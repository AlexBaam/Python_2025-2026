class Product:
    def __init__(self, name, price ):
        self.name = name
        self.price = price

    def price_with_vat(self):
        vat = self.price * 0.19
        return self.price + vat

    def __str__(self):
        return f' Product: {self.name} at the price of:  {self.price_with_vat()}'

class DiscountedProduct(Product):
    def __init__(self, discount, name, price):
        super().__init__(name, price)
        self.discount = discount

    def price_with_vat(self):
        dis_price =self.price -  self.price * self.discount
        vat = dis_price * 0.19
        return dis_price + vat

class ShoppingCart:
    def __init__(self, prod_list):
        self.prod_list = prod_list

    def add_product(self, product):
        self.prod_list.append(product)

    def total_price(self):
        total_price = 0
        for product in self.prod_list:
            total_price += product.price_with_vat()

        return total_price

    def print_prod_list(self):
        for product in self.prod_list:
            print(product)

        print(f'Total price: {self.total_price()}')

Apple = Product('Apple', 100)
Meat = Product('Meat', 200)
DiscountedApple = DiscountedProduct(0.2, 'Disc_Apple', 100)

ShoppingCart = ShoppingCart([Apple,Meat, DiscountedApple])
ShoppingCart.print_prod_list()