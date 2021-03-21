"""
    Creational:
        Factory method
            3 Component => 1.Creator, 2.Product, 3.Client
"""
from abc import abstractmethod


class File:
    def __init__(self, name, file_format):
        self.name = name
        self.file_format = file_format


class B:

    def edit(self, file):  # client
        return self._get_edit(file)

    def _get_edit(self, file):  # creator
        if file.file_format == 'json':  # identifier
            return self.json_edit(file)
        elif file.file_format == 'xml':  # identifier
            return self.xml_edit(file)
        else:
            raise ValueError("So Sorry. . .")

    @abstractmethod
    def json_edit(self, file):  # product
        print(f"Editing Json File. . . {file.name}")

    @abstractmethod
    def xml_edit(self, file):  # product
        print(f"Editing Xml File. . . {file.name}")


if __name__ == '__main__':
    first_file = File('first', 'xml')
    b1 = B()
    b1.edit(first_file)
