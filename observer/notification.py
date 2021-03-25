from abc import ABC, abstractmethod


class Observer(ABC):
    @staticmethod
    @abstractmethod
    def send(message=''):
        pass


class EmailNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"Sending email message : {message}")


class SMSNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f'sending sms massage {message}')


class PushNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f'sending push notification massage {message}')
