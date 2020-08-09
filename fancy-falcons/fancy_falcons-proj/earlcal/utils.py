from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from account.models import Account


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter Earl's birthdays and custom events by day
	def formatday(self, day, earls, events):
		earls_per_day = earls.filter(birthday__day=day)
		events_per_day = events.filter(start_time__day=day)

		d = ''
		for earl in earls_per_day:
			d += f'<br><span class="badge badge-danger">🎂 {earl.get_html_url} </span>'

		for event in events_per_day:
			d += f'<br><span class="badge badge-info"> {event.get_html_url} </span>'

		if day != 0:
			return f"<td><span class='date'>{day}</span>{d}</td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, earls, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, earls, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		earls = Account.objects.filter(birthday__month=self.month)
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		#Creating the table to display 
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, earls, events)}\n'
		cal += '</table>'
		return cal
