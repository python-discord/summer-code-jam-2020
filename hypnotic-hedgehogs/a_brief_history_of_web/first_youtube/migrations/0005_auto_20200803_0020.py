# Generated by Django 3.0.8 on 2020-08-02 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_youtube', '0004_auto_20200803_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 0, 20, 4, 549691)),
        ),
    ]