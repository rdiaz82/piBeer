from django.shortcuts import render
from django.http import HttpResponse
from recipeManager.models import Product
from recipeManager.models import ProductType
from recipeManager.models import Recipe
from recipeManager.models import Ingredient
from .forms import ProductForm
from .forms import ProductFilterForm
from .forms import RecipeFilterForm
from .forms import RecipeForm
from .forms import IngredientForm


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
    filterForm= RecipeFilterForm()
    if recipes.count!=0:
        recipeIngredients=Ingredient.objects.ingredient_by_product_type(recipes[0].id)
    else:
        recipeIngredients={}
    context = {"title": "Recipes",
              "filter_form": filterForm,
              "recipe_list": recipes,
              "newModalTitle": "New Recipe",
              "editModalTitle": "Edit Recipe",
              "deleteModalTitle": "Delete Recipe",
              "deleteModalConfirmation": "Are you sure to delete the recipe?",
              "newIngredientModalTitle":"New Ingredient",
              "deleteIngredientModalTitle":"Are you sure to delete the ingredient?",
              "ingredients":recipeIngredients}
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


def ajax_create_edit_recipe_form(request, recipe_id):
  if (request.method == 'POST'):
    if recipe_id != '-1':
      item = Recipe.objects.get(id=recipe_id)
      form = RecipeForm(request.POST or None, instance=item)
    else:
      form = RecipeForm(request.POST)

    if form.is_valid():
      form.save()
      recipes = Recipe.objects.all()
      response = render(
          request, 'recipeManager/recipeTable.html', {'recipe_list': recipes},)
      return response
    else:
      response = render(
          request, 'recipeManager/modalForm.html', {'form': form}, status=400)
      return response
  else:
    if recipe_id != '-1':
      item = Recipe.objects.get(id=recipe_id)
      form = RecipeForm(instance=item)
    else:
      form = RecipeForm()
    return render(request, 'recipeManager/modalForm.html', {'form': form},)

def ajax_delete_recipe(request,recipe_id):
    Recipe.objects.filter(id=recipe_id).delete()
    recipes = Recipe.objects.all()
    response = render(
        request, 'recipeManager/recipeTable.html', {'recipe_list': recipes},)
    return response

def ajax_filter_recipe(request):
    form=RecipeFilterForm(request.POST)
    if form.is_valid():
        recipe_list = Recipe.objects.all()
        if form.cleaned_data['name']:
            recipe_list=recipe_list.filter(name__icontains=form.cleaned_data['name'])
    else:
        recipe_list=Recipe.objects.all()
    response = render(
        request, 'recipeManager/recipeTable.html', {'recipe_list': recipe_list},)
    return response

def ajax_get_recipe_details(request,recipe_id):
    item = Recipe.objects.get(id=recipe_id)
    recipeIngredients=Ingredient.objects.ingredient_by_product_type(recipe_id)
    response = render(
    request, 'recipeManager/recipeDetails.html', {
    'recipe': item,
    'ingredients':recipeIngredients},)
    return response

def ajax_create_edit_ingredient_form(request,ingredient_id):
    if (request.method == 'POST'):
        print
        if ingredient_id != '-1':
            item = Ingredient.objects.get(id=ingredient_id)
            print (item.quantity)
            form = IngredientForm(request.POST or None)
            if form.is_valid():
                cd=form.cleaned_data
                item.product_id=cd["product"]
                item.unit_id=cd["unit"]
                item.recipe_id=cd["recipe"]
                item.quantity=cd["quantity"]
                print (item.quantity)
                item.save()
            else:
                response = render(
                request, 'recipeManager/modalNewIngredientForm.html', {'form': form}, status=400)
                return response
        else:
            form = IngredientForm(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                print(cd)
                ingredient=Ingredient(quantity=cd["quantity"])
                ingredient.product_id=cd["product"]
                ingredient.unit_id=cd["unit"]
                ingredient.recipe_id=cd["recipe"]
                ingredient.save();
            else:
                response = render(
                request, 'recipeManager/modalNewIngredientForm.html', {'form': form}, status=400)
                return response
        recipeIngredients=Ingredient.objects.ingredient_by_product_type(cd["recipe"])
        response = render(
        request, 'recipeManager/recipeIngredientTable.html', {'ingredients':recipeIngredients},)
        return response

    else:
        if ingredient_id != '-1':
            item = Ingredient.objects.get(id=ingredient_id)
            form = IngredientForm(initial={"product":item.product.id,"quantity":item.quantity,"unit":item.unit.id,"recipe":item.recipe.id})
        else:
            form = IngredientForm()
        return render(request, 'recipeManager/modalNewIngredientForm.html', {'form': form},)
