# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurationManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='is_recipe_unit',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
