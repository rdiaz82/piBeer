from django.shortcuts import render
from django.http import HttpResponse
from recipeManager.models import Product
from .forms import ProductForm


def products(request):
  products = Product.objects.all()
  context = {"title": "Products",
             "product_list": products,
             "newModalTitle": "New Product",
             "editModalTitle": "Edit Product",
             "deleteModalTitle": "Delete Product",
             "deleteModalConfirmation": "Are you sure to delete de product?", }
  return render(request, 'recipeManager/mainProducts.html', context)


def recipes(request):
  return render(request, 'recipeManager/mainRecipes.html')


def ajax_create_product_form(request, product_id=None):
  if (request.method == 'POST'):
    if product_id != None:
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
    if product_id:
      item = Product.objects.get(id=product_id)
      form = ProductForm(instance=item)
    else:
      form = ProductForm()
    return render(request, 'recipeManager/modalForm.html', {'form': form},)
