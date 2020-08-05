
from django.db.models.signals import post_save
from .models import Floppy, VMachine
from django.dispatch import receiver


@receiver(signal=post_save, sender=Floppy)
def create_profile_on_user_creation_or_update(sender,instance,**kwargs):
    if kwargs.get('created', False) is not False:
        instance.vm.floppy_disks_id.append(instance.storage_id)
        instance.vm.floppy_disks_name.append(instance.name)
        instance.vm.save()
    else:
        instance.vm.save()
