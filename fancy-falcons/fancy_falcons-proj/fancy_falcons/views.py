from django.shortcuts import render
from account.models import Account
from datetime import datetime


def home(request):
    # Editing Earl of the Day ID should update all data on home page
    earl_of_the_day_id = 2
    month = datetime.today().month
    upcoming_birthdays = Account.objects.filter(birthday__month=month).order_by('birthday')
    context = {
        "earl_of_the_day": Account.objects.get(pk=earl_of_the_day_id),
        "upcoming": upcoming_birthdays,
        "active_page": "home",
    }
    return render(request, 'home.html', context)
