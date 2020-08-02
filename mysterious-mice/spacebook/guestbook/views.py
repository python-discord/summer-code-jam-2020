from django.shortcuts import render

def guestbook(request):
    return render(request, 'guestbook/guestbook.html', {})