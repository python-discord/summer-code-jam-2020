from django.shortcuts import render
from account.models import Account

def home(request):
    # Editing Earl of the Day ID should update all data on home page
    earl_of_the_day_id = 2
    context = {
        "earl_of_the_day": Account.objects.get(pk=earl_of_the_day_id),
        "active_page": "home",
    }
    return render(request, 'home.html', context)