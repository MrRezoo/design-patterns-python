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


class Singleton(type):
    """
    Singleton metaclass
    Based on Python Cookbook 3rd Edition Recipe 9.13
    Only one instance of a class can exist. Does not work with __slots__
    """

    def __init__(self, *args, **kw):
        super(Singleton, self).__init__(*args, **kw)
        self.__instance = None

    def __call__(self, *args, **kw):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kw)
        return self.__instance

   

   
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
