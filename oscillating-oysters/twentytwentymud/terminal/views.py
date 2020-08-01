from django.shortcuts import render


def terminal(request):
    """Render a simple page with a terminal."""

    return render(request, 'terminal/terminal.html')
