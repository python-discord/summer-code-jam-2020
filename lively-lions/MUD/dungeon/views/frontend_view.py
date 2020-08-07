from django.shortcuts import render
from django.middleware.csrf import get_token


# CSRF for Post Request
# If you post request, you must put the csrf token value in the header X-CSRFToken.
# The csrf token value is stored as a csrftoken cookie.
# Cookies are stored in the user's browser for one year and are generated upon deletion.
##
# https://docs.djangoproject.com/en/3.0/ref/csrf/
# #
# You can communicate with the server as Ajax
# #
def index(request):
    response = render(request, 'dungeon/index.html',)
    csrf_token = get_token(request)
    response.set_cookie(key='csrftoken', value=csrf_token)
    return response
