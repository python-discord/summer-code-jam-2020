from django import http
from django.views.generic.edit import CreateView, UpdateView

from .models import TodoEntry


class TodoEntryCreate(CreateView):
    model = TodoEntry
    template_name = 'todo_create_form.html'
    fields = ['name']
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class TodoEntryUpdate(UpdateView):
    model = TodoEntry
    template_name = 'todo_update_form.html'
    fields = ['name', 'done']
