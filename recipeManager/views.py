from django.shortcuts import render
from django.http import HttpResponse

def products(request):
	return render(request, 'recipeManager/mainProducts.html')

def recipes(request):
	return render(request, 'recipeManager/mainRecipes.html')
