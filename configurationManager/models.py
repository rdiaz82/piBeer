from django.db import models

class Unit(models.Model):
    name=models.CharField(max_length=20)
    symbol=models.CharField(max_length=5)
    is_recipe_unit=models.BooleanField()

    def __str__(self):
        return self.symbol

# Create your models here.
