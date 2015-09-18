# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeManager', '0005_auto_20150914_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='ui_color',
            field=models.CharField(default='info', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='ui_icon',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stepvarimplementation',
            name='var_ingredient',
            field=models.ForeignKey(to='recipeManager.Ingredient', null=True),
        ),
        migrations.AlterField(
            model_name='stepvarimplementation',
            name='var_value',
            field=models.DecimalField(max_digits=6, null=True, decimal_places=2),
        ),
    ]
