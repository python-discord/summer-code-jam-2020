from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    """To avoid logging in/registering again if the user logged in"""
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        # Redirect to their profile if authenticated
        if request.user.is_authenticated:
            return redirect('earlydating-yourprofile')
        # Else authenticate user
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    """Restricting page access to specified user groups"""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    """Restrict page access to only admins"""
    @wraps(view_func)
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'profile':
            return redirect('earlydating-yourprofile')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function
