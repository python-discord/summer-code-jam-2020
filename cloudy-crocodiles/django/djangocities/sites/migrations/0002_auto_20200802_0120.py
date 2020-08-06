# Generated by Django 3.0.8 on 2020-08-02 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='address',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='site',
            unique_together={('city', 'address')},
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=256)),
                ('version', models.CharField(choices=[('H1', 'HTML 1'), ('H2', 'HTML 2')], default='H1', max_length=2)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'pages',
                'unique_together': {('site', 'filename')},
            },
        ),
    ]