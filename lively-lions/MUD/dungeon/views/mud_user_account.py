# from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from dungeon.models.character import MudUser
from django.views import View
from django.db import IntegrityError


class MudUserView(View):
    def post(self, request):
        if request.POST["view_name"] == 'is_working':
            if 'multiple_data' in request.POST:
                return HttpResponse("Working multiple_data POST " + request.POST["multiple_data"])
            return HttpResponse("Working POST " + request.POST["view_name"])
        elif request.POST["view_name"] == 'create_user':
            username = request.POST['username']
            password = request.POST['password']
            user = MudUser(username=username, password=password)
            try:
                user.save()
            except IntegrityError:
                return HttpResponse(user.username + " The ID already exists.")
            else:
                return HttpResponse("Success create User " + user.username)
        else:
            pass

    # def create_account(request):
    # Done !
    #   pass

    # def login_view(request):
    #     user_name = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=user_name, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return HttpResponse(f"Login success")
    #     else:
    #         return HttpResponse(f"Login fail")

    # @login_required
    # def user_profile(request):
    #     return HttpResponse(f"View profile of user: {request.user.id}")

    # @login_required
    # def delete_account(request):
    #     return HttpResponse(f"Delete user: {request.user.id}")
