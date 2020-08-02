from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

from terminal.terminal_tools import colorize
BANNER = """
 #####    ###    #####    ###      #     # #     # ######  
#     #  #   #  #     #  #   #     ##   ## #     # #     # 
      # #     #       # #     #    # # # # #     # #     # 
 #####  #     #  #####  #     #    #  #  # #     # #     # 
#       #     # #       #     #    #     # #     # #     # 
#        #   #  #        #   #     #     # #     # #     # 
#######   ###   #######   ###      #     #  #####  ######  
                Welcome to == 2020 MUD ==
                Where the future is NOW.
                Type "help" for a list of commands
""".replace('\n', '\r\n')


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
            "Your name is " + colorize(name, 'brightBlue') + "\r\n"
            "You are in 2020 MUD\r\n"
            "It is " + str(currDate) 
            )
    elif text == "welcome":
        response = colorize(BANNER, 'brightRed') 
    else:
        response = "I don't understand, try `help`."

    return HttpResponse(response)
