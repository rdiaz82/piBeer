from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^products/$', views.products, name='recipe_manager_products'),
    url(r'^recipes/$', views.recipes, name='recipe_manager_recipes'),
]
