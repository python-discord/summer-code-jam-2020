from django.shortcuts import render
from .forms import Guestbook

def comment(request):
   
   if request.method == "POST":
      #Get the posted form
      guestbook_form = Guestbook(request.POST)
      
      if guestbook_form.is_valid():
         print(guestbook_form.cleaned_data)
   else:
      guestbook_form = Guestbook()
        
#   return render(request, 'loggedin.html', {"username" : username})

def guestbook(request):
    return render(request, 'guestbook/guestbook.html', {})