from django.conf.urls import url

from recipeManager import views

urlpatterns = [
    url(r'^products/$', views.products, name='recipe_manager_products'),
    url(r'^products/create/(?P<product_id>-?[0-9]+)/$', views.ajax_create_edit_product_form, name='recipe_manager_add_edit_product'),
    url(r'^products/delete/(?P<product_id>-?[0-9]+)/$', views.ajax_delete_product, name='recipe_manager_delete_product'),
    url(r'^products/filter/$', views.ajax_filter_product, name='recipe_manager_filter_product'),
    url(r'^recipes/$', views.recipes, name='recipe_manager_recipes'),
    url(r'^recipes/create/(?P<recipe_id>-?[0-9]+)/$', views.ajax_create_edit_recipe_form, name='recipe_manager_add_edit_recipe'),
    url(r'^recipes/delete/(?P<recipe_id>-?[0-9]+)/$', views.ajax_delete_recipe, name='recipe_manager_delete_recipe'),
    url(r'^recipes/filter/$', views.ajax_filter_recipe, name='recipe_manager_filter_recipe'),
    url(r'^recipes/select/(?P<recipe_id>-?[0-9]+)/$', views.ajax_get_recipe_details, name='recipe_manager_get_details'),
    url(r'^recipes/create/ingredient/(?P<recipe_id>-?[0-9]+)/(?P<ingredient_id>-?[0-9]+)/$', views.ajax_create_edit_ingredient_form, name='recipe_manager_add_edit_ingredient'),
]
