# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurationManager', '0001_initial'),
        ('recipeManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(default=1, to='configurationManager.Unit'),
            preserve_default=False,
        ),
    ]
