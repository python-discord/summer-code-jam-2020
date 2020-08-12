from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm


class CalendarView(generic.ListView):
    model = Event
    template_name = 'earlcal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use todays date
        d = get_date(self.request.GET.get('month', None))

        # Create a calendar class instance
        cal = Calendar(d.year, d.month)

        # Formatmonth which returns a html view of the calendar
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['active_page'] = "calendar"
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event_view(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    return render(request, 'earlcal/event_display.html', {"active_page": "calendar", 'event': instance})

@login_required
def event(request, event_id=None):
    instance = Event()
    is_editing = False
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
        is_editing = True

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('earlcal:calendar'))
    return render(request, 'earlcal/event.html', {'form': form, "event": instance, "active_page": "calendar", "editing": is_editing})
