from django.contrib import admin

from .models import Unit

class UnitAdmin(admin.ModelAdmin):
    list_display=('name','symbol','is_recipe_unit')

admin.site.register(Unit,UnitAdmin)
