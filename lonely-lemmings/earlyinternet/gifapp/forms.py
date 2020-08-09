from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Project, Comment


class ProjectForm(forms.Form):
    project_name = forms.CharField(label='New Project', max_length=50)

    def clean_project_name(self):
        """ensure there is no existing project under the user with the same name"""
        project_name = self.cleaned_data["project_name"]
        if Project.objects.filter(name=project_name).exists():
            raise forms.ValidationError("Already existing project name")

        return project_name


class CommentForm(forms.ModelForm):
    """Form for making a comment on a post"""
    content = forms.CharField(label="Comment", widget=forms.TextInput())

    class Meta:
        model = Comment
        fields = ["content"]


class UserRegisterForm(UserCreationForm):
    # required=True is default
    email = forms.EmailField(required=True)

    # whenever the form validates, it will create a new User
    # the model that will be affected is the User model
    class Meta:
        model = User
        # order in which fields should be displayed
        fields = ['username', 'email', 'password1', 'password2']
