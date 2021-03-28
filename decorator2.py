"""
    Structural :
        Decorator => decorator pattern != python decorator
"""


class Article:
    def show_article(self):
        print(f"All articles . . .{self.__class__}")


class Login:
    def check_login(self, name, password):
        if name == 'reza' and password == 'mr':
            return True
        return f"{self.__class__} dont have access"


def login_decorator(func):
    def wrapper():
        name = input("Enter your name . . .")
        password = input("Enter your password . . .")
        login = Login()
        result = login.check_login(name, password)
        if result:
            func()
        else:
            print('username or password is wrong')

    return wrapper


@login_decorator
def show_all_articles():
    article = Article()
    article.show_article()


show_all_articles()
