from django.shortcuts import render, redirect


def user(request, user_id):
    # user_obj = User.objects.get(pk=user_id)
    # return render(request, 'user/user.html', {'user': user_obj})
    return render(request, 'users/user.html')
