import json
from functools import wraps
from django.views.decorators import require_http_methods


def jsonbody(func):

    @wraps(func)
    @require_http_methods(['POST'])
    def wrapper(request, *args, **kwargs):
        data = json.loads(request.body.decode())
        return func(request, data, *args, **kwargs)
