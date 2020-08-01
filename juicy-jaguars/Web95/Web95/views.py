from django.shortcuts import render, redirect


def landing_page(request):
    """Landing Page view."""
    return render(request,
                  "Web95/landing_page.html")


def index(request):
    """Redirect from index.html to /."""
    return redirect(landing_page)
