"""
    Behavioral pattern:
        Iterator => 1.Iterable 2.Iteration

    Requirements that should know:
        __iter__ , __next__
"""


class Iteration:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        if self.value == 0:
            raise StopIteration('End of sequence')
        for item in range(0, self.value):
            value = self.value
            self.value -= 1
            return value


class Iterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return Iteration(self.value)


if __name__ == '__main__':
    f1 = Iterable(5)
    f2 = iter(f1)

    print(next(f2))
    print(next(f2))
    print(next(f2))
    print(next(f2))
    print(next(f2))
    """we add raise error that don't show later than zero """
    print(next(f2))
