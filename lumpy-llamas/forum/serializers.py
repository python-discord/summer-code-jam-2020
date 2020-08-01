from django.core import serializers
from .models import Thread, ThreadMessage

serialized_threads = serializers.serialize('json', Thread.objects.all())
serialized_messages = serializers.serialize('json', ThreadMessage.objects.all())

