# Generated by Django 3.1 on 2020-08-08 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MUD', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='room_date',
            new_name='server_date',
        ),
    ]