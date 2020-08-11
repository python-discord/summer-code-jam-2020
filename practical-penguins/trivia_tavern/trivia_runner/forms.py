from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import PhoneNumber


class PhoneNumberForm(forms.ModelForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = PhoneNumber
        fields = ['phone_number']
