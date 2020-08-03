import jwt
import datetime

from django.conf import settings
from djangocities.user.models import CustomUser as User

SECRET_KEY = settings.SECRET_KEY

def encode_auth_token(**kwargs):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=0),
        'iat': datetime.datetime.utcnow()
    }

    for key, value in kwargs.items():
        payload[key] = value

    return jwt.encode(
        payload,
        SECRET_KEY
    )


def load_user(info):
    token = decode_auth_token(info.context)
    print(token)
    return User.query.get(token['id'])


def decode_auth_token(request):
    auth_token = request.headers.get('Authorization')
    print('decode')
    print(auth_token)
    secret = SECRET_KEY
    print(secret)
    if not auth_token:
        auth_token = ''
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
