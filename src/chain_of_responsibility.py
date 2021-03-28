"""
    Behavioral pattern:
        Chain of responsibility
"""

from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self.process_request(request)
        if not handled:
            self._successor.handle(request)

    @abstractmethod
    def process_request(self, request):
        pass


# -----------------------------------------------------------------
class HandlerOne(AbstractHandler):
    def process_request(self, request):
        if 0 < request <= 10:
            print(f'Handler One is processing this request... {request}')
            return True


class HandlerTwo(AbstractHandler):
    def process_request(self, request):
        if 10 < request <= 20:
            print(f'Handler Two is processing this request... {request}')
            return True


class DefaultHandler(AbstractHandler):
    def process_request(self, request):
        print(
            f'This request has no handler so default handler is processing '
            f'this request... {request}')
        return True


# -----------------------------------------------------------------
class Client:
    def __init__(self):
        self.handler = HandlerOne(HandlerTwo(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


request = [3, 14, 34, 9]

c1 = Client()
c1.delegate(request)
