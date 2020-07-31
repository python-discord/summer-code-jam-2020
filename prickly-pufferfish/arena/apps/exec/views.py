from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.urls import resolve
import json

# WARNING: Delete in production
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        request_data = request.POST

        return HttpResponse('Good Job!')

    else:
        error = json.dumps({
            'status': 405,
            'error': 'Method Not Allowed',
            'message': 'Http request must be a POST request',
            'path': resolve(request.path_info).url_name
        })
        return HttpResponseNotAllowed(['POST'], error)
