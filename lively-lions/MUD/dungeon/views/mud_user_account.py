# from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
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
            # save() before : should be set_password()
            user.set_password(password)
            try:
                user.save()
            except IntegrityError:
                return HttpResponse(user.username + " The ID already exists.")
            else:
                return HttpResponse("Success create User " + user.username)
        # login
        elif request.POST["view_name"] == 'login_user':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Login success")
            else:
                return HttpResponse("invalid")
        # check login
        elif request.POST["view_name"] == 'login_check':
            if request.user.is_authenticated:
                return HttpResponse("Logged in")
            else:
                return HttpResponse("invalid")
        # get_username # must before login
        elif request.POST["view_name"] == 'get_username':
            if request.user.is_authenticated:
                return HttpResponse(request.user.username)
            else:
                return HttpResponse("invalid")
        # logout
        elif request.POST["view_name"] == 'logout_user':
            if request.user.is_authenticated:
                user = MudUser.objects.get(pk=request.user.pk)
                user.now_connected_character_name = ''
                user.save()
            logout(request)
            return HttpResponse("Logout success")
        else:
            pass

    # def create_account(request):
    # Done !
    #   pass

    # def login_view(request):
    #     Done!
    #   pass

    # @login_required
    # def user_profile(request):
    #     return HttpResponse(f"View profile of user: {request.user.id}")

    # @login_required
    # def delete_account(request):
    #     return HttpResponse(f"Delete user: {request.user.id}")
