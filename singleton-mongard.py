"""
   Creational:
        Singleton
"""


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class DB(metaclass=Singleton):
    pass


if __name__ == '__main__':
    s1 = DB()
    s2 = DB()
    s3 = DB()

    print(id(s1))
    print(id(s2))
    print(id(s3))

    print(id(s1) == id(s2) == id(s3))
