import django.forms as forms
from vmachine.models import Floppy, VMachine


class FloppyCreateForm(forms.ModelForm):
    VirtualMachine = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = Floppy
        fields = ['name', 'VirtualMachine']

    def __init__(self, *args, **kwargs):
        if kwargs.get('user', False) is not False:
            user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['VirtualMachine'].queryset = VMachine.objects.filter(user=user)
