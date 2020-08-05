from django.contrib.staticfiles.views import serve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from core.helpers import jsonbody


def index(request):
    res = serve(request, 'index.html')
    res.set_cookie('csrftoken', get_token(request))
    return res


@jsonbody
def register_endpoint(request, data):
    user = User.objects.create_user(
        data['username'],
        password=data['password'],
    )
    login(request, user)

    return JsonResponse({
        'id': user.id,
        'username': user.username,
    }, status=201)


@jsonbody
def login_endpoint(request, data):
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({
            'id': user.id,
            'username': user.username,
        })
    return JsonResponse({'msg': 'Failed to login'}, status=401)
