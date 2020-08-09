from django.contrib.staticfiles.views import serve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from core.helpers import jsonbody


def index(request):
    res = serve(request, 'index.html')
    res.set_cookie('csrftoken', get_token(request))
    return res


REGISTER_LOGIN_SCHEMA = {
    'type': 'object',
    'required': ['username', 'password'],
    'properties': {
        'username': {
            'type': 'string',
            'minLength': 1,
        },
        'password': {
            'type': 'string',
            'minLength': 1,  # just for the jam, make things quicker
        },
    },
}


@jsonbody(REGISTER_LOGIN_SCHEMA)
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


@jsonbody(REGISTER_LOGIN_SCHEMA)
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


def logout_endpoint(request):
    logout(request)
    return JsonResponse({'msg': 'Successfully logged out'})
