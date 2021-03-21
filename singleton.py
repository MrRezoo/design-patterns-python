class Singleton:

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton()

    print(id(s1))
    print(id(s2))
    print(id(s3))

    print(id(s1) == id(s2) == id(s3))
