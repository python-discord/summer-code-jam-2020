# Generated by Django 3.0.8 on 2020-08-05 12:59

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('shells', models.CharField(choices=[('sh', 'Sh'), ('bash', 'Bash'), ('zsh', 'Zsh')], max_length=4)),
                ('floppy_disks_id', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('floppy_disks_name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Floppy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('storage_id', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]