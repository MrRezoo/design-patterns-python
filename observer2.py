"""
    Behavioral pattern :
	    Observer

	Example :
	    use in django and flask Signal
"""


class Observer:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Observer):
    """changing class"""

    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class One:
    """love to listen changing"""

    def update(self, subject):
        print(f'{subject.name} new {subject.data}')


class Two:
    """love to listen changing"""

    def update(self, subject):
        print(f'{subject.name} new {subject.data}')


if __name__ == '__main__':
    d1 = Data('first')
    d2 = Data('second')
    o = One()
    t = Two()

    d1.attach(o)
    d2.attach(t)

    d1.data = 5
    d2.data = 3
