from django.shortcuts import render
from .models import Board

# Create your views here.

def forumspage(request):
    '''
    Forums home page, displays all message boards, with information
    such as the total number of posts in each board.
    '''
    context = {'boards': Board.objects.all()}
    return render(request, "forums/forum.html", context)
