from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse('This page is working!')
