from django.db.models.signals import post_save, pre_delete, post_delete
from .models import Floppy, VMachine
from django.dispatch import receiver
from the_htvms.runner.disk import create_disk, delete_disk


@receiver(signal=post_save, sender=Floppy)
def assign_floppy_to_vm(sender: Floppy, instance: Floppy, **kwargs: dict) -> None:
    """
    The VM model has two ArrayFields that stores floppy ids, and names, this
    signal will actually assign the Floppies to the VMs
    """
    if kwargs.get('created', False) is not False:
        instance.vm.floppy_disks_id.append(instance.storage_id)
        instance.vm.floppy_disks_name.append(instance.name)
        instance.vm.save()
    else:
        instance.vm.save()


@receiver(signal=post_save, sender=VMachine)
def create_floppy_on_vm_creation(sender: VMachine, instance: VMachine, **kwargs: dict) -> None:
    """
    That function creates a root floppy on VM creation
    Then django will automatically call the assign_floppy_to_vm signal
    """
    if kwargs.get('created', False) is not False:
        # Creates a floppy, and assign an ID.
        floppy = Floppy(name=f"Root Floppy for {instance.name}", user=instance.user,
                        vm=instance, storage_id=create_disk(type_='rom'))
        floppy.save()


@receiver(signal=pre_delete, sender=Floppy)
def delete_floppy_from_vm(sender: Floppy, instance: Floppy, **kwargs: dict) -> None:
    """
    This Signal will unassign the Floppies from the VMs however, the only way to delete floppies
    is to delete the VM itself.
    """
    delete_disk(instance.storage_id)
    del instance.vm.floppy_disks_id[instance.vm.floppy_disks_id.index(instance.storage_id)]
    del instance.vm.floppy_disks_name[instance.vm.floppy_disks_name.index(instance.name)]
    instance.vm.save()
