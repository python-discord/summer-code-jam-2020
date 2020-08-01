from django.contrib.staticfiles.views import serve

# Create your views here.

def index(request):
    return serve(request, 'index.html')
