"""
    Creational :
        Abstract Factory
"""

from abc import ABC, abstractmethod


class ProductBase(ABC):
    """
    this class in Product Factory Class
    """

    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass

    # @abstractmethod
    # def shipping(self):
    #     pass


class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass


class RugsDetail(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"rugs detail: {self.rugs._name}"


class RugsPrice(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"rugs price: {self.rugs._price}"


class GiftCardDetail(DetailBase):
    def __init__(self, card):
        self.giftCard = card

    def show(self):
        return f"company : {self.giftCard.company},"


class GiftCardPrice(DetailBase):
    def __init__(self, card):
        self.giftCard = card

    def show(self):
        return f"gift card min price : {self.giftCard.min_price},max price : " \
               f"{self.giftCard.max_price} "


class Rugs(ProductBase):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def detail(self):
        return RugsDetail(self)

    @property
    def price(self):
        return RugsPrice(self)


class GiftCard(ProductBase):

    def __init__(self, company, min_price, max_price):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price

    @property
    def detail(self):
        return GiftCardDetail(self)

    @property
    def price(self):
        return GiftCardPrice(self)


if __name__ == '__main__':
    r1 = Rugs('persian', 135)
    r2 = Rugs('armani', 155)

    g1 = GiftCard("google", 20, 50)
    g2 = GiftCard("Apple", 40, 100)

    products = [r1, r2, g1, g2]
    for product in products:
        print(product.detail.show())
        print(product.price.show())
