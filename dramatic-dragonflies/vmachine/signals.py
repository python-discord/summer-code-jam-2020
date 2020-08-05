from django.db.models.signals import post_save
from .models import Floppy, VMachine
from django.dispatch import receiver


@receiver(signal=post_save, sender=Floppy)
def assign_floppy_to_vm(sender: Floppy, instance: Floppy, **kwargs: dict) -> None:
    if kwargs.get('created', False) is not False:
        instance.vm.floppy_disks_id.append(instance.storage_id)
        instance.vm.floppy_disks_name.append(instance.name)
        instance.vm.save()
    else:
        instance.vm.save()


@receiver(signal=post_save, sender=VMachine)
def create_floppy_on_vm_creation(sender: VMachine, instance: VMachine, **kwargs: dict) -> None:
    if kwargs.get('created', False) is not False:
        # Below there, instead of "12fdsdf" for storage_id a
        # function attached to Floppy's save method will generate one.
        floppy = Floppy(name="Root Floppy for " + str(instance.name), user=instance.user, vm=instance,
                        storage_id="12fdsdf")
        floppy.save()
