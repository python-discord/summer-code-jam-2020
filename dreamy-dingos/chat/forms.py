from django import forms

class RoomNameForm(forms.Form):
    room_name = forms.CharField(label='Room name', max_length=50)