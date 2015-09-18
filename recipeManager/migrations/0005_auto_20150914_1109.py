# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeManager', '0004_auto_20150914_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steptype',
            name='additional_vars',
            field=models.ManyToManyField(to='recipeManager.StepDefinition', blank=True),
        ),
    ]
