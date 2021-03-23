"""
    Creational :
        Prototype
"""
from copy import deepcopy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prototype:
    def __init__(self):
        self._object = {}

    def register(self, name, obj):
        self._object[name] = obj

    def unregister(self, name):
        del self._object[name]

    def clone(self, name, **kwargs):
        cloned_obj = deepcopy(self._object.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


if __name__ == '__main__':
    p1 = Person('reza', 20)
    pro1 = Prototype()
    pro1.register(name='person1', obj=p1)
    personCopy = pro1.clone(name='person1')

    """ sample test """
    print(personCopy.name is p1.name)
    print(personCopy.age is p1.age)
    print(id(personCopy.name))
    print(id(p1.name))

    """ update keyword arguments """
    personCopy = pro1.clone(name='person1', age=43)
    print(personCopy.age, personCopy.name)
