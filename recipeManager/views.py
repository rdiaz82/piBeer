from django.shortcuts import render
from django.http import HttpResponse
from recipeManager.models import Product
from recipeManager.models import Recipe
from .forms import ProductForm
from .forms import ProductFilterForm
from .forms import IngredientFilterForm


def products(request):
  products = Product.objects.all()
  filterForm= ProductFilterForm()
  context = {"title": "Products",
             "filter_form": filterForm,
             "product_list": products,
             "newModalTitle": "New Product",
             "editModalTitle": "Edit Product",
             "deleteModalTitle": "Delete Product",
             "deleteModalConfirmation": "Are you sure to delete the product?", }
  return render(request, 'recipeManager/mainProducts.html', context)


def recipes(request):
    recipes = Recipe.objects.all()
    filterForm= IngredientFilterForm()
    context = {"title": "Recipes",
              "filter_form": filterForm,
              "recipe_list": recipes,
              "newModalTitle": "New Product",
              "editModalTitle": "Edit Product",
              "deleteModalTitle": "Delete Product",
              "deleteModalConfirmation": "Are you sure to delete the product?", }
    return render(request, 'recipeManager/mainRecipes.html',context)


def ajax_create_edit_product_form(request, product_id):
  if (request.method == 'POST'):
    if product_id != '-1':
      item = Product.objects.get(id=product_id)
      form = ProductForm(request.POST or None, instance=item)
    else:
      form = ProductForm(request.POST)

    if form.is_valid():
      form.save()
      products = Product.objects.all()
      response = render(
          request, 'recipeManager/productTable.html', {'product_list': products},)
      return response
    else:
      response = render(
          request, 'recipeManager/modalForm.html', {'form': form}, status=400)
      return response
  else:
    if product_id != '-1':
      item = Product.objects.get(id=product_id)
      form = ProductForm(instance=item)
    else:
      form = ProductForm()
    return render(request, 'recipeManager/modalForm.html', {'form': form},)

def ajax_delete_product(request,product_id):
    Product.objects.filter(id=product_id).delete()
    products = Product.objects.all()
    response = render(
        request, 'recipeManager/productTable.html', {'product_list': products},)
    return response

def ajax_filter_product(request):
    form=ProductFilterForm(request.POST)
    if form.is_valid():
        list = Product.objects.all()
        if form.cleaned_data['name']:
            list=list.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['product_type']:
            list=list.filter(product_type=form.cleaned_data['product_type'])
    else:
        list=Product.objects.all()
    response = render(
        request, 'recipeManager/productTable.html', {'product_list': list},)
    return response
