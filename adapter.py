from abstract_factory import Rugs


class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        return self.rate * product._price


if __name__ == '__main__':
    r1 = Rugs('persian rugs', 1200)
    r2 = Rugs('persian rugs', 1500)
    r3 = Rugs('persian rugs', 1100)

    adapter = PriceAdapter(rate=20000)

    rugs = [r1, r2, r3]

    for rug in rugs:
        print(f"{rug._name}:{adapter.exchange(rug)}")
