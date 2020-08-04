from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from vmachine.models import VMachine

# Create your views here.


def index(request: HttpRequest, storage_id: int, vm_id: int) -> HttpResponse:
    virtual_machine = VMachine.objects.get(pk=vm_id)
    if virtual_machine.user != request.user:
        return redirect('home')
    return render(request, 'terminal/index.html')
