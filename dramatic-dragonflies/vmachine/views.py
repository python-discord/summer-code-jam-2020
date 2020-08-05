from django.shortcuts import render, reverse
from vmachine.models import VMachine
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.forms import Form


class VMCreateView(LoginRequiredMixin, CreateView):
    model = VMachine
    fields = ['name', 'shells']
    template_name = "users/create_vm.html"
    success_url = 'disks'

    def form_valid(self, form: Form) -> object:
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
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
            first_action = reverse('index', kwargs={
                'storage_id': vm.floppy_disks_id[0],
                'vm_id': vm.pk
            })
            vm.__dict__['add_zips'] = add_zips
            vm.__dict__['first_action'] = first_action
        return render(request, 'users/disks.html', {'object_list': user_virtual_machines})
