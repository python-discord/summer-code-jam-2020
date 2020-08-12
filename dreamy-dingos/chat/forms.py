from django import forms


class RoomNameForm(forms.Form):
    room_name = forms.CharField(label='Room name', max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
