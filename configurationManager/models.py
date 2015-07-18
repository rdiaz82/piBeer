from django.db import models

class Unit(models.Model):
    name=models.CharField(max_length=20)
    symbol=models.CharField(max_length=5)

    def __str__(self):
        return self.name

# Create your models here.
