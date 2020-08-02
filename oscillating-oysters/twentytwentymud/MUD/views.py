from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

# ANSI Color codes for the terminal, make sure to reset after using
COLOR = {
    'reset': '\x1b[0m',
    'black': '\x1b[30m',
    'red': '\x1b[31m',
    'green': '\x1b[32m',
    'yellow': '\x1b[33m',
    'blue': '\x1b[34m',
    'magenta': '\x1b[35m',
    'cyan': '\x1b[36m',
    'white': '\x1b[37m',
    'brightBlack': '\x1b[1;30m',
    'brightRed': '\x1b[1;31m',
    'brightGreen': '\x1b[1;32m',
    'brightYellow': '\x1b[1;33m',
    'brightBlue': '\x1b[1;34m',
    'brightMagenta': '\x1b[1;35m',
    'brightCyan': '\x1b[1;36m',
    'brightWhite': '\x1b[1;37m',
}

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
            "Your name is " + COLOR['brightRed'] + name + COLOR['reset'] + "\r\n"
            "You are in 2020 MUD\r\n"
            "It is " + str(currDate) 
            )
    elif text == "welcome":
        response = COLOR['brightBlue'] + BANNER + COLOR['reset']
    else:
        response = "I don't understand, try `help`."

    return HttpResponse(response)
