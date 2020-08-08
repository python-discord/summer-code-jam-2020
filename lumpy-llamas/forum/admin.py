from django.contrib import admin

# Register your models here.
from .models import Thread, ThreadMessage

admin.site.register(Thread)
admin.site.register(ThreadMessage)
