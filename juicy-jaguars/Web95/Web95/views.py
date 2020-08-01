from django.shortcuts import render, redirect

def landing_page(request):
    return render(request,
                  "Web95/landing_page.html")
