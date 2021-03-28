"""
    Creational :
        Builder => every builders designed patterns has director class to attach
                   each side of objects
"""


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        wheel = self.__builder.get_wheel()
        car.set_wheel(wheel)

        engine = self.__builder.get_engine()
        car.set_engine(engine)
        return car


# ----------------------------------------
class Car:
    def __init__(self):
        self.__wheel = None
        self.__engine = None
        self.__body = None

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def set_body(self, body):
        self.__body = body

    def set_engine(self, engine):
        self.__engine = engine

    def detail(self):
        print(f'Body: {self.__body.shape}')
        print(f'Engine: {self.__engine.hp}')
        print(f'Wheel: {self.__wheel.size}')


# ----------------------------------------
class Builder:
    def get_engine(self):
        pass

    def get_wheel(self):
        pass

    def get_body(self):
        pass


class Benz(Builder):
    def get_body(self):
        body = Body()
        body.shape = 'Suv'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel


class Bmw(Builder):
    def get_body(self):
        body = Body()
        body.shape = 'Sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel


# ----------------------------------------
class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    hp = None


# ----------------------------------------


car1 = Bmw()
director = Director()
director.set_builder(car1)
b1 = director.get_car()
b1.detail()
