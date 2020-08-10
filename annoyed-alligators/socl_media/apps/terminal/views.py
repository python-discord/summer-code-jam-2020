from django.shortcuts import render
from django.http import HttpResponse
from .command_runner import TerminalCommandRunner


def index(request):
    return render(request, 'terminal.html')


def run_terminal_command(request):
    """
    This view handles the request and response of the commands.
    It takes in the request, sends it to command_runner for running,
    and then sends back the command's response to the template.
    """

    command = request.GET.get('c', None)
    if command is None:
        response = "No command was specified"
        status = 400
    else:
        command_runner = TerminalCommandRunner(command, request)
        result = command_runner.run(**request.headers)
        status = 200
        response = HttpResponse(result['response'], status=status)

        if 'redirect' in result:
            response['redirect'] = result['redirect']

        if 'followup' in result:
            response['followup'] = True

    return response
