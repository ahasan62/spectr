# Generated by Django 4.1.3 on 2022-11-27 20:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normalized',
            name='normalized',
        ),
        migrations.AddField(
            model_name='normalized',
            name='normalized_float',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='normalized',
            name='isocode',
            field=models.CharField(default='', max_length=50),
        ),
    ]
