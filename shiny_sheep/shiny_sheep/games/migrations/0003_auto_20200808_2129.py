# Generated by Django 3.0.8 on 2020-08-09 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200808_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='game_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]