# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-02 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent',
            name='name',
            field=models.CharField(max_length=765),
        ),
        migrations.AlterField(
            model_name='coordinatesystem',
            name='short_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='empire',
            name='name',
            field=models.CharField(max_length=765),
        ),
        migrations.AlterField(
            model_name='inempire',
            name='empire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Empire'),
        ),
        migrations.AlterField(
            model_name='inempire',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.State'),
        ),
        migrations.AlterField(
            model_name='inregion',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Location'),
        ),
        migrations.AlterField(
            model_name='inregion',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Region'),
        ),
        migrations.AlterField(
            model_name='instate',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Location'),
        ),
        migrations.AlterField(
            model_name='instate',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.State'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=765),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=765),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=765),
        ),
    ]
