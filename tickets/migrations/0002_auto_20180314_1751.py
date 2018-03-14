# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-14 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='account',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='aging_batch',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='clinic',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cpt_codes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='escalate_to',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='insurance',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='patient_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='preventive_action',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='statusA',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='worked',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
