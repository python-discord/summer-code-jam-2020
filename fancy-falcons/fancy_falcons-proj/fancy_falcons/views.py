from django.shortcuts import render
from account.models import Account
from datetime import datetime


def home(request):
    # Editing Earl of the Day ID should update all data on home page
    earl_of_the_day_id = 2
    upcoming_birthdays = Account.objects.filter(birthday__gte=datetime.now()).order_by('birthday')[:3]
    context = {
        "earl_of_the_day": Account.objects.get(pk=earl_of_the_day_id),
        "upcoming": upcoming_birthdays,
        "active_page": "home",
    }
    return render(request, 'home.html', context)
