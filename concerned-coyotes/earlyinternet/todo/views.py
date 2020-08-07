from django.views.generic.edit import CreateView, UpdateView

from .models import TodoEntry


class TodoEntryCreate(CreateView):
    model = TodoEntry
    template_name = 'todo_create_form.html'
    fields = ['name']


class TodoEntryUpdate(UpdateView):
    model = TodoEntry
    template_name = 'todo_update_form.html'
    fields = ['name', 'done']
