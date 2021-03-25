from time import sleep


class LazyLoader:
    """
    we write lazy that when we need object initialize this
    not when we create object
    """

    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


class MySQLHandler:
    def __init__(self):
        sleep(1)

    def connect(self):
        return "connect to MySQL"


class MongoHandler:
    def __init__(self):
        sleep(10)

    def get(self):
        return "Hello from Mongo"


class NotificationCenterHandler:
    def __init__(self):
        sleep(1)

    def show(self):
        return "Hello from notif center"


if __name__ == '__main__':
    mysql = LazyLoader(MySQLHandler)
    mongo = LazyLoader(MongoHandler)
    notification = LazyLoader(NotificationCenterHandler)

    print(mysql.connect())
    print(notification.show())
    print(mongo.get())
    print(mysql.connect())
    print(notification.show())
    print(mysql.connect())
    print(notification.show())
    print(mysql.connect())
    print(notification.show())
    print(mongo.get())
