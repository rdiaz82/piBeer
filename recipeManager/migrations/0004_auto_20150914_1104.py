# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeManager', '0003_init_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('order', models.IntegerField()),
                ('recipe', models.ForeignKey(to='recipeManager.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='StepDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('var_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StepType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('additional_vars', models.ManyToManyField(to='recipeManager.StepDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='StepVarImplementation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('var_value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('step', models.ForeignKey(to='recipeManager.Step')),
                ('var_name', models.ForeignKey(to='recipeManager.StepDefinition')),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='step_type',
            field=models.ForeignKey(to='recipeManager.StepType'),
        ),
    ]
