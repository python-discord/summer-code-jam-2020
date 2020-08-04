from django.shortcuts import render, reverse
from vmachine.models import VMachine
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpRequest


def vmachine_list(request: HttpRequest) -> HttpResponse:

    # Checks if the user has any VMachines,
    # if not it will add an additional context field, that the template will handle.
    try:
        user_virtual_machines = VMachine.objects.filter(user=request.user)
    except ObjectDoesNotExist:
        user_virtual_machines = None
    if user_virtual_machines is None:
        return render(request, 'users/disks.html', {'is_empty': True})
    else:
        # Zips the storage_id and storage_name ArrayFields, for further use in  templates.
        # Adds, the first action that's always based on the first field of the storage_id
        # Array and storage_name Arrays.
        for vm in user_virtual_machines:
            add_zips = zip(vm.floppy_disks_id, vm.floppy_disks_name)
            first_action = reverse('terminal_non_socket_url', kwargs={
                'storage_id': vm.floppy_disks_id[0],
                'vm_id': vm.pk
            })
            vm.__dict__['add_zips'] = add_zips
            vm.__dict__['first_action'] = first_action
        return render(request, 'users/disks.html', {'object_list': user_virtual_machines})
