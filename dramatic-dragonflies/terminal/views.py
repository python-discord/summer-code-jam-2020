from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from vmachine.models import VMachine, Floppy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.


def index(request: HttpRequest, storage_id: int, vm_id: int) -> HttpResponse:
    try:
        virtual_machine = VMachine.objects.get(pk=vm_id)
    except ObjectDoesNotExist:
        virtual_machine = None
    if virtual_machine is not None:
        if virtual_machine.user != request.user:
            messages.error(request, "That's not your VirtualMachine!")
            return redirect('home')
        else:
            floppy = Floppy.objects.get(storage_id=storage_id)
            if floppy.user == request.user:

                return render(request, 'terminal/index.html')
            else:
                messages.error(request, "That's not your Floppy!")
                return redirect('home')
    else:
        messages.error("Virtual Machine not found")
        return redirect('home')
