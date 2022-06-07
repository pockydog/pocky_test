from functools import wraps
from flask import request


class PayloadUtils:
    @staticmethod
    def inspect_schema(schema=None):
        def real_decorator(method, **kwargs):
            @wraps(method)
            def wrapper(*args, **kwargs):
                if request.method in {'GET', 'DELETE'}:
                    payload = request.args
                    payload = dict(payload)
                else:
                    payload = request.get_json(force=True)
                if schema:
                    schema.validate(payload)
                return method(*args, **kwargs, payload=payload)

            return wrapper

        return real_decorator
