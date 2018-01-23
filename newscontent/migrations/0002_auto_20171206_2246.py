# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscontent',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='newscontent',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]