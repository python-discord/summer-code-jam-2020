# Generated by Django 3.0.8 on 2020-07-31 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='time',
            new_name='timestamp',
        ),
    ]
