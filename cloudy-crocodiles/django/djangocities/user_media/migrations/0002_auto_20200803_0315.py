# Generated by Django 3.0.8 on 2020-08-03 03:15

from django.db import migrations, models
import djangocities.user_media.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='directory',
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(upload_to=djangocities.user_media.models.upload_to),
        ),
    ]