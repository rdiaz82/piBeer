from django.contrib import admin

from .models import ProductType
from .models import Product
from .models import Recipe
from .models import Ingredient
from .models import Step
from .models import StepType
from .models import StepDefinition
from .models import StepVarImplementation

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type','description')

class IngredientAdmin(admin.ModelAdmin):
    list_display=('recipe','product','quantity','unit')

class RecipeAdmin(admin.ModelAdmin):
    list_display=('name','description')

class StepAdmin(admin.ModelAdmin):
    list_display=('order','recipe','step_type')

class StepTypeAdmin(admin.ModelAdmin):
    list_display=('name','ui_color','ui_icon')

class StepDefinitionAdmin(admin.ModelAdmin):
    list_display=('var_name',)

class StepVarImplementationAdmin(admin.ModelAdmin):
    list_display=('step','var_name','var_value')


admin.site.register(ProductType,ProductTypeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(Step,StepAdmin)
admin.site.register(StepType,StepTypeAdmin)
admin.site.register(StepDefinition,StepDefinitionAdmin)
admin.site.register(StepVarImplementation,StepVarImplementationAdmin)
