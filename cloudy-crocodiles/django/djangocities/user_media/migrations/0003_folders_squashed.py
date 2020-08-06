# Generated by Django 3.0.9 on 2020-08-05 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('user_media', '0003_auto_20200805_0143'), ('user_media', '0004_auto_20200805_0150'), ('user_media', '0005_auto_20200805_0151'), ('user_media', '0006_auto_20200805_0153'), ('user_media', '0007_auto_20200805_0154'), ('user_media', '0008_auto_20200805_0154'), ('user_media', '0009_auto_20200805_0157'), ('user_media', '0010_auto_20200805_0217'), ('user_media', '0011_auto_20200805_0221'), ('user_media', '0012_auto_20200805_0228'), ('user_media', '0013_auto_20200805_0231')]

    dependencies = [
        ('user_media', '0002_auto_20200803_0315'),
        ('sites', '0005_delete_page'),
        ('folders', '0009_remove_folder_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='filename',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folders.Folder'),
        ),
    ]