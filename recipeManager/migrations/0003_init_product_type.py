# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def product_type(apps, schema_editor):

    ProductType = apps.get_model("recipeManager", "ProductType")

    product = ProductType(id=1, name="Malt")
    product.save()

    product = ProductType(id=2, name="Hop")
    product.save()

    product = ProductType(id=3, name="Yeast")
    product.save()

    product = ProductType(id=4, name="Aditive")
    product.save()

    product = ProductType(id=5, name="Other")
    product.save()

    product = ProductType(id=1, name="Malt")
    product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('recipeManager', '0002_ingredient_unit'),
    ]

    operations = [
        migrations.RunPython(product_type),
    ]
