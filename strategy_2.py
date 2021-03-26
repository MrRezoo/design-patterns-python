from abc import ABC, abstractmethod

ALLOWED_EXTENSIONS = ["html", 'csv', 'mp3', 'mp4', 'txt']


class AbstractRenderer(ABC):
    @abstractmethod
    def render(self):
        pass


class HTMLRenderer(AbstractRenderer):
    def render(self):
        print("Render using HTMLRenderer")


class MP3Renderer(AbstractRenderer):
    def render(self):
        print("Render using MP3Renderer")


class MP4Renderer(AbstractRenderer):
    def render(self):
        print("Render using MP4Renderer")


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    @property
    def extension(self):
        return self.filename.split('.')[-1]

    @classmethod
    def create(cls, filename):
        if filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
            print("File extension not allowed")
        return cls(filename)

    def render(self):
        handler_dict = {
            'html': HTMLRenderer,
            'mp3': MP3Renderer,
            'mp4': MP4Renderer
        }
        handler = handler_dict[self.extension]
        return handler().render()


if __name__ == '__main__':
    f1 = FileHandler.create('doc.mp4')
    f2 = FileHandler.create('doc.html')
    f3 = FileHandler.create('doc.pdf')
    f4 = FileHandler.create('doc.mp3')

    files_list = [f1, f2, f4]
    for file_name in files_list:
        file_name.render()
