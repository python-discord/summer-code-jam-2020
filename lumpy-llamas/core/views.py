from django.contrib.staticfiles.views import serve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from core.helpers import jsonbody


def index(request):
    return serve(request, 'index.html')


@jsonbody
def register(request, data):
    user = User.create_user(
        data['username'],
        email=data['email'],
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
