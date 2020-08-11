# from django.shortcuts import render
# from django.middleware.csrf import get_token
# from .models import Item_Category, Small_Item, Large_Item
from django.http import HttpResponse

# Create your views here.

"""
POST is generating
GET is importing
"""


class CRUD:
    # CRUD

    def rest(request, self):

        # Read
        if request.method == "GET":
            return HttpResponse("Working GET")
        # Create
        if request.method == "POST":
            if request.POST["num"]:
                return HttpResponse("Working POST " + request.POST["num"])
            else:
                return HttpResponse("Working POST")
