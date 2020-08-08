from django.contrib import admin
from django.forms import NumberInput
from django.db import models
from .models import Rover


class RoverModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {"widget": NumberInput(attrs={"size": "10"})}
    }


admin.site.register(Rover, RoverModelAdmin)
