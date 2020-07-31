from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def terminal(request):
    """Render a simple page with a terminal.

    It should send any input to command() for processing and print out
    any response."""

    return render(request, 'terminal/terminal.html')


# TODO I used csrf_exempt here, take it out when I figure out how to
# do the POST properly
@csrf_exempt
def command(request, text):
    """Process commands from the terminal."""
    if text == "help":
        response = ("Commands:\r\n"
            "help - this help\r\n"
            "something - something else")

    else:
        response = "I don't understand, try `help`."

    return HttpResponse(response)
