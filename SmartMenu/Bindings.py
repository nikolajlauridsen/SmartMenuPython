from functools import wraps


class Bindings:
    def __init__(self):
        self.bindings = {}

    def bind(self, f_id):
        def decorator(func):
            self.bindings[f_id] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def call_binding(self, f_id):
        self.bindings[f_id]()

