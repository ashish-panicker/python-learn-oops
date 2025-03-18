from payment import VisaPayment

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product_name):
        self.items = [item for item in self.items if item[0].name != product_name]

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def apply_discount(self, discount):
        total = self.calculate_total()
        return total - (total * discount / 100)

    def display_cart(self):
        for product, quantity in self.items:
            print(f"{product} x {quantity}")
