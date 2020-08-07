from django.shortcuts import render
from django.http import HttpResponse

from .methods import TerminalCommand
# Create your views here.


def index(request):
    return render(request, 'terminal.html')


def run_terminal_command(request):
    command = request.GET.get('c', None)
    if command is None:
        response = "No command was specified"
        status = 400
    else:
        run_command = TerminalCommand(command)
        result = run_command.run(**request.headers)
        status = 200
        response = HttpResponse(result['response'], status=status)
        if 'followup' in result:
            response['followup'] = True
    return response
