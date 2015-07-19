from django.conf.urls import url

from recipeManager import views

urlpatterns = [
    url(r'^products/$', views.products, name='recipe_manager_products'),
    url(r'^products/create/$', views.ajax_create_product_form, name='recipe_manager_add_product'),
    url(r'^products/create/(?P<product_id>[0-9]+)/$', views.ajax_create_product_form, name='recipe_manager_edit_product'),
    url(r'^recipes/$', views.recipes, name='recipe_manager_recipes'),

]
