from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from vmachine.models import VMachine, Floppy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.


def _home_with_error(request: HttpRequest, error_msg: str) -> HttpResponse:
    messages.error(request, error_msg)
    return redirect('home')


def test(request: HttpRequest) -> HttpResponse:
    return render(request, 'terminal/index.html', dict(vm_id=0, storage_id=0))


def index(request: HttpRequest, storage_id: int, vm_id: int) -> HttpResponse:
    try:
        virtual_machine = VMachine.objects.get(pk=vm_id)
    except ObjectDoesNotExist:
        return _home_with_error(request, "Virtual Machine not found")
    else:
        if virtual_machine.user != request.user:
            return _home_with_error(request, "That's not your VirtualMachine!")
        else:
            try:
                floppy = Floppy.objects.get(storage_id=storage_id)
            except ObjectDoesNotExist:
                return _home_with_error(request, "Floppy not found")
            else:
                if floppy.user != request.user:
                    return _home_with_error(request, "That's not your Floppy!")
                else:
                    return render(request, 'terminal/index.html', dict(storage_id=storage_id, vm_id=vm_id))
