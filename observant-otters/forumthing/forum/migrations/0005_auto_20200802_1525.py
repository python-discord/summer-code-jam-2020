# Generated by Django 3.0.8 on 2020-08-02 22:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200802_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]