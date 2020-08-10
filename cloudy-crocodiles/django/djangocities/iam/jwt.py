import jwt
import datetime
import logging

from django.conf import settings
from djangocities.user.models import CustomUser as User

SECRET_KEY = settings.SECRET_KEY


def encode_auth_token(**kwargs):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=0),
        "iat": datetime.datetime.utcnow(),
    }

    for key, value in kwargs.items():
        payload[key] = value

    return jwt.encode(payload, SECRET_KEY)


def load_user(info):
    request = info.context["request"]
    token = decode_auth_token(request)
    return User.objects.get(id=token["id"])


def decode_auth_token(request):
    auth_token = request.headers.get("Authorization")
    if auth_token.startswith("Bearer "):
        auth_token = auth_token.split(" ", 1)[1]
    logging.debug(f"decode {auth_token}")
    secret = SECRET_KEY
    if not auth_token:
        auth_token = ""
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again."
    except jwt.InvalidTokenError:
        return f"Invalid token {auth_token}. Please log in again."
