from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime


# TODO I used csrf_exempt here, take it out when I figure out how to
# do the POST properly
@csrf_exempt
def process_command(request, text):
    """Process commands from the terminal."""

    if text == "help":
        response = (
            "Commands:\r\n"
            "    help\r\n"
            "    status"
            )
    elif text == "status":
        # TODO get proper player name
        name = "Deckard"
        currDate = datetime.datetime.now()
        response = (
            "Your name is " + name + "\r\n"
            "You are in 2020 MUD\r\n"
            "It is " + str(currDate) 
            )
    else:
        response = "I don't understand, try `help`."

    return HttpResponse(response)
