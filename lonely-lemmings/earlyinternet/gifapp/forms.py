from django import forms
from .models import Project


class ProjectForm(forms.Form):
    project_name = forms.CharField(label='New Project', max_length=50)

    def clean_project_name(self):
        """ensure there is no existing project under the user with the same name"""
        project_name = self.cleaned_data["project_name"]
        print(project_name)
        if Project.objects.filter(name=project_name).exists():
            raise forms.ValidationError("Already existing project name")

        return project_name
