"""
    Structural :
        Decorator
"""


COUNTRIES = ['Iran', 'UAE']
VAT = {'Iran': 9, 'UAE': 15}


class User:
    pass


class Address:
    def __init__(self, country):
        self.country = country


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.products_list = []

    def add_product_list(self, product_list):
        if not isinstance(product_list, list):
            product_list = [product_list]
        self.products_list.extend(product_list)

    def total_price(self):
        result = 0
        for product in self.products_list:
            result += product.price
        return result


def calculate_vat(func):
    def wrapped_func(purchase_item):
        vat = VAT[purchase_item.address.country]
        total_price = purchase_item.total_price()
        return total_price + total_price * vat / 100

    return wrapped_func


def show_total_price(purchase_item):
    return purchase_item.total_price()


@calculate_vat
def show_vat_plus_price(purchase_item):
    return purchase_item.total_price()


if __name__ == '__main__':
    user = User()
    add_iran = Address(country=COUNTRIES[0])
    add_uae = Address(country=COUNTRIES[1])

    p1 = Product('persian rug', 145)
    p2 = Product('uae rug', 160)
    p3 = Product('turk rug', 180)
    products = [p1, p2, p3]

    purchase_iran = Purchase(user=user, address=add_iran)
    purchase_uae = Purchase(user=user, address=add_uae)

    purchase_iran.add_product_list(p1)
    purchase_uae.add_product_list(p1)
    purchase_iran.add_product_list([p2, p3])
    purchase_uae.add_product_list([p2, p3])
    print(show_total_price(purchase_iran))
    print(show_total_price(purchase_uae))
    print(show_vat_plus_price(purchase_iran))
    print(show_vat_plus_price(purchase_uae))
