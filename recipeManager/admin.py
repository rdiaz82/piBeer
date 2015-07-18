from django.contrib import admin

from .models import ProductType
from .models import Product
from .models import Recipe
from .models import Ingredient

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type','description')

class IngredientAdmin(admin.ModelAdmin):
    list_display=('recipe','product','quantity')

class RecipeAdmin(admin.ModelAdmin):
    list_display=('name','description')

admin.site.register(ProductType,ProductTypeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Ingredient,IngredientAdmin)
