from django.shortcuts import render, reverse, redirect
from vmachine.models import VMachine
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView
from django.forms import Form
from django.contrib import messages
from .forms import FloppyCreateForm


@login_required
def create_floppy(request: HttpRequest):
    if request.method == "GET":
        if VMachine.objects.filter(user=request.user).count() == 0:
            messages.error("You don't have any Virtual Machines that you could create floppy for!")
            return redirect('disks')
        else:
            form = FloppyCreateForm(user=request.user)
            return render(request, 'users/create_floppy.html', {'form': form})
    else:
        if VMachine.objects.filter(user=request.user).count() == 0:
            messages.error("You don't have any Virtual Machines that you could create floppy for!")
            return redirect('disks')
        else:
            form = FloppyCreateForm(request.POST, user=request.user)
            if form.is_valid():
                form.instance.storage_id = "1212ads" # Will delete
                form.instance.user = request.user
                form.instance.vm = form.cleaned_data['VirtualMachine']
                form.save()
            messages.success(request, 'Floppy successfully created!')
            return redirect('disks')


class VMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VMachine
    success_url = '/users/disks'
    template_name = "users/vmachine_confirm_delete.html"

    def test_func(self):
        form_vmachine_object = self.get_object()
        if self.request.user == form_vmachine_object.user:
            return True
        return False

    def handle_no_permission(self):
        messages.error('You have no permission to do this!')
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
    # Checks if the user has any VMachines,
    # if not it will add an additional context field, that the template will handle
    check_vm = VMachine.objects.filter(user=request.user).count()
    if check_vm == 0:
        return render(request, 'users/disks.html', {'is_empty': True})
    else:
        user_virtual_machines = VMachine.objects.filter(user=request.user)
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
