from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def terminal(request):
    """Render a simple page with a terminal."""

    return render(request, 'terminal/terminal.html')
