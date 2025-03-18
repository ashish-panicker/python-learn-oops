class Order:
    def __init__(self, cart):
        self.cart = cart

    def checkout(self, discount=0):
        total = self.cart.apply_discount(discount)
        return f"Order placed! Total after {discount}% discount: ${total:.2f}"
