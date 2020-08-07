from django.views.generic.edit import CreateView

from .models import TodoEntry


class TodoEntryCreate(CreateView):
    model = TodoEntry
    template_name = 'todo_create_form.html'
    fields = ['name']
