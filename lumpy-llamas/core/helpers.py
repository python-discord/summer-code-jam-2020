import json
from functools import wraps
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseBadRequest
from fastjsonschema import validate, JsonSchemaException


def jsonbody(schema):

    def decorator(func):

        @wraps(func)
        @require_http_methods(['POST'])
        def wrapper(request, *args, **kwargs):
            data = json.loads(request.body.decode())
            try:
                validated_data = validate(schema, data)
                return func(request, validated_data, *args, **kwargs)
            except JsonSchemaException as ex:
                return HttpResponseBadRequest(ex.message)
        return wrapper
    return decorator
