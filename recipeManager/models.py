from django.db import models


class ProductType(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product (models.Model):
    name=models.CharField(max_length=100)
    product_type=models.ForeignKey(ProductType)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Recipe (models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Ingredient (models.Model):
    product=models.ForeignKey(Product)
    quantity=models.DecimalField(max_digits=6, decimal_places=2)
    unit=models.ForeignKey('configurationManager.Unit',limit_choices_to={'is_recipe_unit': True})
    recipe=models.ForeignKey(Recipe)

    def __str__(self):
        return self.product.name
