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
def create_floppy(request: HttpRequest) -> HttpResponse:
    # In case of GET request, it checks if the user has any vm, if not it renders an error page, otherwise
    # a page with the floppy creation form.
    if request.method == "GET":
        if VMachine.objects.filter(user=request.user).count() == 0:
            messages.error(request, "You don't have any Virtual Machines that you could create floppy for!")
            return redirect('disks')
        else:
            form = FloppyCreateForm(user=request.user)
            return render(request, 'users/create_floppy.html', {'form': form})
    # Do the same in case of POST request.
    else:
        if VMachine.objects.filter(user=request.user).count() == 0:
            messages.error(request, "You don't have any Virtual Machines that you could create floppy for!")
            return redirect('disks')
        else:
            # Checks if the given VM is a valid vm, and if it belongs to the user that made the request.
            form = FloppyCreateForm(request.POST, user=request.user)
            if form.is_valid():
                if VMachine.objects.filter(pk=form.cleaned_data['VirtualMachine'].pk).count() == 0:
                    messages.error(request, "The given VM is not valid.")
                    return redirect('disks')
                vm = VMachine.objects.get(pk=form.cleaned_data['VirtualMachine'].pk)
                if vm.user == request.user:
                    form.instance.user = request.user
                    form.instance.vm = form.cleaned_data['VirtualMachine']
                    form.save()
                else:
                    messages.error(request, "This is not your VM!")
                    return redirect("disks")
                messages.success(request, 'Floppy successfully created!')
            return redirect('disks')


class VMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VMachine
    success_url = '/users/disks'
    template_name = "users/vmachine_confirm_delete.html"

    def test_func(self) -> bool:
        form_vmachine_object = self.get_object()
        if self.request.user == form_vmachine_object.user:
            return True
        return False

    # Sends an error message, if a user is trying to delete someone else's VM
    def handle_no_permission(self) -> HttpResponse:
        messages.error(self.request, 'You have no permission to do this!')
        return redirect(reverse('home'))


class VMCreateView(LoginRequiredMixin, CreateView):
    model = VMachine
    fields = ['name', 'shells']
    template_name = "users/create_vm.html"
    success_url = 'disks'

    def form_valid(self, form: Form) -> object:
        form.instance.user = self.request.user
        form.instance.pk = 1260
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
