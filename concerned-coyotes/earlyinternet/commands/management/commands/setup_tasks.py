from django.core.management.base import BaseCommand
from django_q.models import Schedule


class Command(BaseCommand):
    help = "Setups up all background tasks"

    def handle(self, *args, **options):
        Schedule.objects.get_or_create(
            func='news.tasks.get_news',
            schedule_type='D',
            repeats=-1
        )
        self.stdout.write('Add task to fetch news')

        Schedule.objects.get_or_create(
            func='wikipedia.tasks.fetch_wikipedia',
            schedule_type='D',
            repeats=-1
        )
        self.stdout.write('Add task to fetch wikipedia articles')

        Schedule.objects.get_or_create(
            func='weather.tasks.fetch_weather',
            schedule_type='D',
            repeats=-1
        )
        self.stdout.write('Add task to fetch weather')
