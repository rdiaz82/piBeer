# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeManager', '0009_stepdefinition_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepdefinition',
            name='use_ingredient',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stepdefinition',
            name='use_value',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
