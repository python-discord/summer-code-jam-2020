from django.shortcuts import render, reverse, redirect
from vmachine.models import VMachine
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView
from django.forms import Form
from django.contrib import messages
from .forms import FloppyCreateForm
from the_htvms.runner.disk import create_disk


def _disks_with_error(request: HttpRequest, error_msg: str) -> HttpResponse:
    messages.error(request, error_msg)
    return redirect('disks')


@login_required
def create_floppy(request: HttpRequest) -> HttpResponse:
    """
    if the user has any vm, redirect to the floppy creation form, otherwise render an error page
    """
    if VMachine.objects.filter(user=request.user).count() == 0:
        return redirect('disks')
    if request.method == "GET":
        form = FloppyCreateForm(user=request.user)
        return render(request, 'users/create_floppy.html', {'form': form})
    elif request.method == "POST":
        # Checks if the given VM is a valid vm, and if it belongs to the user that made the request.
        form = FloppyCreateForm(request.POST, user=request.user)
        if form.is_valid():
            if VMachine.objects.filter(pk=form.cleaned_data['VirtualMachine'].pk).count() == 0:
                return _disks_with_error(request, "The given VM is not valid.")
            vm = VMachine.objects.get(pk=form.cleaned_data['VirtualMachine'].pk)
            if vm.user == request.user:
                form.instance.user = request.user
                form.instance.vm = form.cleaned_data['VirtualMachine']
                form.instance.storage_id = create_disk(type_='blank')
                form.save()
            else:
                return _disks_with_error(request, "This is not your VM!")
            messages.success(request, 'Floppy successfully created!')
        return redirect('disks')


class VMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VMachine
    success_url = '/users/disks'
    template_name = "users/vmachine_confirm_delete.html"

    def test_func(self) -> bool:
        form_vmachine_object = self.get_object()
        return self.request.user == form_vmachine_object.user

    def handle_no_permission(self) -> HttpResponse:
        """
        Send an error message if a user is trying to delete someone else's VM
        """
        messages.error(self.request, 'You have no permission to do this!')
        return redirect(reverse('home'))


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
    """
    the list of all VMs of a user
    if the user has no VMachines, add an additional context field the template will handle
    """
    user_virtual_machines = VMachine.objects.filter(user=request.user)
    if user_virtual_machines.count() == 0:
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
