# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurationManager', '0001_initial'),
        ('recipeManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('date_init', models.DateField()),
                ('date_end', models.DateField(null=True, blank=True)),
                ('recipe', models.ForeignKey(to='recipeManager.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('batch', models.ForeignKey(to='brewery.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('content', models.CharField(max_length=500)),
                ('batch', models.ForeignKey(to='brewery.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('unit', models.ForeignKey(to='configurationManager.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(to='brewery.Sensor'),
        ),
    ]
