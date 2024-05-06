"""
   Creational:
        Singleton
"""


class Singleton1(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class Singleton2(type):
    """
    Singleton metaclass
    Based on Python Cookbook 3rd Edition Recipe 9.13
    Only one instance of a class can exist. Does not work with __slots__
    """

    def __init__(self, *args, **kw):
        super(Singleton2, self).__init__(*args, **kw)
        self.__instance = None

    def __call__(self, *args, **kw):
        if self.__instance is None:
            self.__instance = super(Singleton2, self).__call__(*args, **kw)
        return self.__instance


class DBMongo(metaclass=Singleton2):
    pass

class DBPostgres(metaclass=Singleton2):
    pass


if __name__ == '__main__':
    m1 = DBMongo()
    m2 = DBMongo()

    p1 = DBPostgres()
    p2 = DBPostgres()

    print(f"Mongo: {id(m1)} - {id(m2)} ", id(m1) == id(m2))
    print(f"Postgres: {id(p1)} - {id(p2)} ", id(p1) == id(p2))
