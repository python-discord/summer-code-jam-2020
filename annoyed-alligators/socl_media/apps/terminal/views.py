from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

import random
import json

from .methods import TerminalCommand
# Create your views here.

def index(request):
    # names = ("bob", "dan", "jack", "lizzy", "susan")
    # items = []
    # for i in range(100):
    #     items.append({
    #         "name": random.choice(names),
    #         "age": random.randint(20, 80),
    #         "url": "https://example.com",
    #     })

    # context = {}
    # context["items"] = json.dumps(items)
    return render(request, 'terminal.html')


def terminal_command(request):
    command = request.GET.get('c', None)
    if command is None:
        response = "No command was specified"
        status = 400
    else:
        run_command = TerminalCommand(command)
        response = run_command.run()
        status = 200
    return HttpResponse(response, status=status)