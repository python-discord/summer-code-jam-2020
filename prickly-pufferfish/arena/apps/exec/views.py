from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
import json


def index(request):
    request = HttpRequest()
    
    if request.method == "POST":
        request_data = request.POST
        return HttpResponse("Good Job!")
        
    else:
        return HttpResponseBadRequest("POST request required")

