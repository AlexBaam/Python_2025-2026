from e02 import Product

class Invoice:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.sell_all()

        return total

    def opposite_of_cheapest(self):
        first_product = self.products[0]

        for product in self.products[1:]:
            if product.price > first_product.price:
                first_product = product

        first_product.describe()

    def print_invoice(self):
        for product in self.products:
            product.describe()

        print("Total price: ", self.total_value())

apple = Product("Apple", 4, 10)
orange = Product("Orange", 5, 10)
meat = Product("Meat", 6, 10)

products_list = [apple, orange]
invoice = Invoice(products_list)
invoice.print_invoice()

invoice.add_product(meat)
invoice.print_invoice()

invoice.opposite_of_cheapest()


