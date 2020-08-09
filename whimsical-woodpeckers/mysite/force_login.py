from django.contrib.auth import authenticate, login


def force_authenticate(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.user.is_authenticated:
            user = authenticate(request)
            if user:
                login(request, user)

        response = get_response(request)

        return response

    return middleware
