# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0005_siteuser_zip_zode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='phone',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='zip_zode',
            field=models.CharField(default=0, max_length=5),
        ),
    ]
