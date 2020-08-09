from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('earlcal:event_view', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
