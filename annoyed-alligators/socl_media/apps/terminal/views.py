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
        response = run_command.run()
        status = 200
    return HttpResponse(response, status=status)
