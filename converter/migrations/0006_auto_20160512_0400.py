# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0005_shape_number3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shape',
            name='number1',
        ),
        migrations.RemoveField(
            model_name='shape',
            name='number2',
        ),
        migrations.RemoveField(
            model_name='shape',
            name='number3',
        ),
        migrations.AlterField(
            model_name='shape',
            name='measurement',
            field=models.CharField(default='area', max_length=34),
        ),
        migrations.AlterField(
            model_name='shape',
            name='shape',
            field=models.CharField(max_length=34),
        ),
    ]
