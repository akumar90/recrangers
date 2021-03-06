# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20170306_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecAreas',
            fields=[
                ('keywords', models.CharField(max_length=100)),
                ('lastupdateddate', models.CharField(max_length=100)),
                ('orgrecareaid', models.CharField(max_length=100)),
                ('recareadescription', models.CharField(max_length=100000)),
                ('recareadirections', models.CharField(max_length=100000)),
                ('recareaemail', models.CharField(max_length=500)),
                ('recareafeedescription', models.CharField(max_length=100000)),
                ('recareaid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('recarealatitude', models.CharField(max_length=100)),
                ('recarealongitude', models.CharField(max_length=100)),
                ('recareamapurl', models.CharField(max_length=100)),
                ('recareaname', models.CharField(max_length=1000)),
                ('recareaphone', models.CharField(max_length=1000)),
                ('recareareservationurl', models.CharField(max_length=1000)),
                ('staylimit', models.CharField(max_length=20)),
            ],
        ),
    ]
