from django.test import TestCase
from .models import Event
import datetime

class CalendarModelTests(TestCase):

    def test_all_events_have_valid_dates(self):
        eventslist = Event.objects.all()
        validDate = True
        for event in eventlist:
            try:
                _ = datetime.datetime(event.start_time)
                _ = datetime.datetime(event.end_time)
            except ValueError:
                validDate = False
        self.assertTrue(validDate)
