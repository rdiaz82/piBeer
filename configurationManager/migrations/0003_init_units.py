# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def units(apps, schema_editor):

    Unit = apps.get_model("configurationManager", "Unit")

    unit = Unit(id=1, name="Weight", symbol="g", is_recipe_unit=True)
    unit.save()

    unit = Unit(id=2, name="Volume", symbol="L", is_recipe_unit=True)
    unit.save()

    unit = Unit(id=3, name="Units", symbol="units", is_recipe_unit=True)
    unit.save()

    unit = Unit(id=4, name="Temperature", symbol="º", is_recipe_unit=True)
    unit.save()

    unit = Unit(id=1, name="Density", symbol=" ", is_recipe_unit=True)
    unit.save()

class Migration(migrations.Migration):

    dependencies = [
        ('configurationManager', '0002_unit_is_recipe_unit'),
    ]

    operations = [
        migrations.RunPython(units),
    ]
