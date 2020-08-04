import datetime
from django.shortcuts import render
from django.http import HttpResponse
from anon.models import AnonUser

# Create your views here.


def get_user(request):
    print(request.session)
    id = request.session.get("ID")
    if not id:
        user = AnonUser.objects.create(last_seen=datetime.datetime.now())
        request.session['ID'] = user.id
    else:
        user = AnonUser.objects.get(id=id)


    return HttpResponse("hello" + str(vars(user)))



