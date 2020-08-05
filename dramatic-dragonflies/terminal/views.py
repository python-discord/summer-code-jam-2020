from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from vmachine.models import VMachine
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request: HttpRequest, storage_id: int, vm_id: int) -> HttpResponse:
    try:
        virtual_machine = VMachine.objects.get(pk=vm_id)
    except ObjectDoesNotExist:
        virtual_machine = None
    if virtual_machine is not None:
        if virtual_machine.user != request.user:
            return redirect('home')
        return render(request, 'terminal/index.html')
    else:
        return redirect('home')
