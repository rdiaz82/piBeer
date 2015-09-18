# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeManager', '0006_auto_20150917_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='ui_color',
        ),
        migrations.RemoveField(
            model_name='step',
            name='ui_icon',
        ),
        migrations.AddField(
            model_name='steptype',
            name='ui_color',
            field=models.CharField(default='info', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='steptype',
            name='ui_icon',
            field=models.CharField(default='ion-fire', max_length=30),
            preserve_default=False,
        ),
    ]
