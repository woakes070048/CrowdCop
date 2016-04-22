# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdcop_web', '0017_auto_20160412_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='details',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tip',
            name='suspect_hair_style',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('SHORT', 'Short'), ('MEDIUM', 'Medium'), ('LONG', 'Long'), ('DREADLOCKS', 'Dreadlocks'), ('BALDING', 'Balding'), ('BALD/SHAVED', 'Bald/Shaved'), ('OTHER', 'Other')], max_length=30),
        ),
    ]
