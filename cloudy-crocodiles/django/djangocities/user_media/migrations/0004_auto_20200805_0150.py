# Generated by Django 3.0.9 on 2020-08-05 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_media', '0003_auto_20200805_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='parent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_media.Media'),
        ),
    ]
