# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-31 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdcop_web', '0007_contribution_crowdcopuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPalID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.IntegerField()),
            ],
        ),
    ]