# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdcop_web', '0023_auto_20160412_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypalid',
            name='contact_info',
            field=models.TextField(verbose_name='How can we contact you?'),
        ),
        migrations.AlterField(
            model_name='paypalid',
            name='contact_name',
            field=models.CharField(max_length=100, verbose_name='Your Name (not required):'),
        ),
        migrations.AlterField(
            model_name='paypalid',
            name='paypal_username',
            field=models.CharField(max_length=100, verbose_name='If you wish to be compensated for your tip, please enter your Paypal username here (Not Required):'),
        ),
    ]
