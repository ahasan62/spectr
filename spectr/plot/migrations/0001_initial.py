# Generated by Django 4.1.2 on 2022-10-23 20:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molecule', models.CharField(default='', max_length=8)),
                ('isocode', models.IntegerField(default=1)),
                ('velocity', models.FloatField()),
                ('thermal', models.FloatField()),
                ('profile', models.CharField(default='', max_length=50, unique=True)),
                ('temperature', models.FloatField()),
                ('log_columndensity', models.FloatField()),
                ('emission', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Normalized',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molecule', models.CharField(default='', max_length=8)),
                ('isocode', models.IntegerField(default=1221)),
                ('velocity', models.FloatField()),
                ('thermal', models.FloatField()),
                ('profile', models.CharField(default='', max_length=50, unique=True)),
                ('temperature', models.FloatField()),
                ('log_columndensity', models.FloatField(default=1)),
                ('normalized', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=1), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Wavelength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oversampling', models.FloatField()),
                ('resolution', models.FloatField()),
                ('wavelength', models.FloatField(default=0)),
            ],
        ),
    ]
