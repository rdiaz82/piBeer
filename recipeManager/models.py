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

class IngredientManager(models.Manager):
    def ingredient_by_product_type(self, recipe_id):
        productsType=ProductType.objects.all().order_by('name')
        recipeProducts={}
        for simpleType in productsType:
            recipeIngredients=self.filter(recipe_id=recipe_id,product__product_type=simpleType)
            if recipeIngredients.count()!=0:
                recipeProducts[simpleType.name]=recipeIngredients
        return recipeProducts


class Ingredient (models.Model):
    product=models.ForeignKey(Product)
    quantity=models.DecimalField(max_digits=6, decimal_places=2)
    unit=models.ForeignKey('configurationManager.Unit',limit_choices_to={'is_recipe_unit': True})
    recipe=models.ForeignKey(Recipe)
    objects=IngredientManager()

    def __str__(self):
        return self.product.name


class StepManager(models.Manager):
    def steps_for_recipe(self, recipe_id):
        steps=self.filter(recipe_id=recipe_id).order_by('order')
        print('numero de pasos:',steps.count())
        completeStepList=[]
        for simpleStep in steps:
            completeStep={}
            completeStep['step']=simpleStep
            completeStep['additional_vars']=StepVarImplementation.objects.filter(step_id=simpleStep.id)
            completeStepList.append(completeStep)
        print (completeStepList)
        return completeStepList


class StepDefinition(models.Model):
    var_name=models.CharField(max_length=100)
    unit=models.ForeignKey('configurationManager.Unit')
    use_value=models.BooleanField()
    use_ingredient=models.BooleanField()

    def __str__(self):
        return self.var_name


class StepType (models.Model):
    name=models.CharField(max_length=100)
    additional_vars=models.ManyToManyField(StepDefinition, blank=True)
    ui_color=models.CharField(max_length=30)
    ui_icon=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Step (models.Model):
    order=models.IntegerField()
    recipe=models.ForeignKey(Recipe)
    step_type=models.ForeignKey(StepType)
    objects=StepManager()


class StepVarImplementation(models.Model):
    step=models.ForeignKey(Step)
    var_name=models.ForeignKey(StepDefinition)
    var_value=models.DecimalField(max_digits=6, decimal_places=2, null=True,blank=True)
    var_ingredient=models.ForeignKey(Ingredient, null=True, blank=True)
