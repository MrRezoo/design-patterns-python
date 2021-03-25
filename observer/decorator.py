def notify_observers(message=''):
    def decorator_method(func):
        def wrapped(obj, *arg, **kwargs):
            result = func(obj, *arg, **kwargs)
            for observer in obj.observers:
                observer.send(message)
            return result

        return wrapped

    return decorator_method
