# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

# from mud.dungeon.models.character import MudUser


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

# def create_account(request):
#     user_name = request.POST['username']
#     password = request.POST['password']
#     user = MudUser.objects.create_user(username=user_name, password=password)
#     if user is not None:
#         return HttpResponse(f"Create new user with name: {user_name} success")
#     else:
#         return HttpResponse(f"Create new user with name: {user_name} failure")

# @login_required
# def delete_account(request):
#     return HttpResponse(f"Delete user: {request.user.id}")
