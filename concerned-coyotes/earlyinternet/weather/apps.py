from django.apps import AppConfig


class WeatherConfig(AppConfig):
    name = 'weather'

    def ready(self):
        from django.conf import settings
        if settings.TESTING:
            return

        from django_q.models import Schedule
        Schedule.objects.get_or_create(
            func='weather.tasks.fetch_weather',
            schedule_type='D',
            repeats=-1
        )
