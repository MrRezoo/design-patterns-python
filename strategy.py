class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Gateway:
    def __init__(self, name):
        self.name = name


class Payment:
    gateway = (Gateway('G2'), Gateway('G1'))

    def __init__(self, purchase):
        self.purchase = purchase

    def get_gateway(self):
        return self.gateway[0] if self.purchase.total_price() < 100 else \
            self.gateway[1]

    def pay(self):
        """if payment amount is less than 100,use G1 gateway otherwise use G2"""
        gateway = self.get_gateway()
        print(f"payment is being paid through {gateway.name}")


class Purchase:
    def __init__(self):
        self.products = list()
        self.payment = Payment(self)

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum([p.price for p in self.products])

    def checkout(self):
        self.payment.pay()


if __name__ == '__main__':
    p1 = Product('p1', 40)
    p2 = Product('p1', 50)
    p3 = Product('p1', 20)

    purchase = Purchase()
    purchase.add_product(p1)
    print(purchase.total_price())
    purchase.checkout()

    purchase.add_product(p2)
    print(purchase.total_price())
    purchase.checkout()

    purchase.add_product(p3)
    print(purchase.total_price())
    purchase.checkout()
