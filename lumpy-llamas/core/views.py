from django.contrib.staticfiles.views import serve


def index(request):
    return serve(request, 'index.html')
