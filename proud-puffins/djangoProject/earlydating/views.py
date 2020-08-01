from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1>Early Dating Home Page</h1>'
                        '<p>'
                        '<a href="about">About page</a>'
                        '</p>'
                        '<p>'
                        '<a href="admin">Admin page</a>'
                        '</p>')


def about(request):
    return HttpResponse('<h1>Early Dating Home Page -- About</h1>')
