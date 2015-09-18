# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeManager', '0007_auto_20150917_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepvarimplementation',
            name='var_ingredient',
            field=models.ForeignKey(null=True, blank=True, to='recipeManager.Ingredient'),
        ),
        migrations.AlterField(
            model_name='stepvarimplementation',
            name='var_value',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]
