from django.db import models

class Batch(models.Model):
    name=models.CharField(max_length=40)
    date_init=models.DateField()
    date_end=models.DateField(null=True, blank=True)
    recipe=models.ForeignKey('recipeManager.Recipe')

    def __str__(self):
        return self.name


class Note(models.Model):
    date=models.DateField()
    content=models.CharField(max_length=500)
    batch=models.ForeignKey(Batch)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=50)
    unit=models.ForeignKey("configurationManager.Unit")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    date=models.DateField()
    batch=models.ForeignKey(Batch)
    sensor=models.ForeignKey(Sensor)
    value=models.DecimalField(max_digits=5, decimal_places=2)
