import django.forms as forms
from vmachine.models import Floppy, VMachine


class FloppyCreateForm(forms.ModelForm):
    VirtualMachine = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = Floppy
        fields = ['name', 'VirtualMachine']

    # the form is called with an additional user object, that we fetched from the kwargs dict, then deleted it.
    # then set the VirtualMachine modelchoicefield so that it'll only contain the user's virtualmachines.

    def __init__(self, *args: list, **kwargs: dict) -> None:
        if kwargs.get('user', False) is not False:
            user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['VirtualMachine'].queryset = VMachine.objects.filter(user=user)
