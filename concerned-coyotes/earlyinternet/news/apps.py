from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        from django.conf import settings
        if settings.TESTING:
            return

        # Create the Task for fetching the news
        # only if it does not exist yet
        from django_q.models import Schedule
        Schedule.objects.get_or_create(
            func='news.tasks.get_news',
            schedule_type='D',
            repeats=-1
        )
