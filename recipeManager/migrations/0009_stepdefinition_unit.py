# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurationManager', '0003_init_units'),
        ('recipeManager', '0008_auto_20150917_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepdefinition',
            name='unit',
            field=models.ForeignKey(to='configurationManager.Unit', default=1),
            preserve_default=False,
        ),
    ]
