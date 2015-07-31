from django.forms import ModelForm, TextInput, Select, Textarea, HiddenInput
from django.forms.models import ModelChoiceIterator, ModelChoiceField
from recipeManager.models import Product
from recipeManager.models import ProductType
from recipeManager.models import Recipe
from recipeManager.models import Ingredient
from configurationManager.models import Unit
from django import forms

def get_product_choices():
    product_choices=list()
    all_product_type=ProductType.objects.all()
    for product_type in all_product_type:
        sub_array=list()
        all_products=Product.objects.filter(product_type=product_type)
        for simple_product in all_products:
            single_product=(simple_product.id,simple_product.name)
            sub_array.append(single_product)
        complete_category=(product_type.name,sub_array)
        product_choices.append(complete_category)
    return product_choices

def get_unit_choices():
    unit_choices=list()
    all_units=Unit.objects.filter(is_recipe_unit=True)
    for unit in all_units:
        unit_definition=(unit.id,unit.symbol)
        unit_choices.append(unit_definition)
    return unit_choices

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'product_type': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control','col':3,'row':3}),
        }

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control','col':3,'row':3}),
        }

class ProductFilterForm(forms.Form):
    name=forms.CharField(max_length=50,required=False, widget=forms.TextInput(attrs={'class': "form-control col-lg-3"}))
    product_type=forms.ModelChoiceField(queryset=ProductType.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control col-lg-3'}))

class RecipeFilterForm(forms.Form):
    name=forms.CharField(max_length=50,required=False, widget=forms.TextInput(attrs={'class': "form-control col-lg-3"}))

class IngredientForm(forms.Form):
    product=forms.ChoiceField(label='Product',choices=get_product_choices(), widget=Select(attrs={'class': "form-control"}))
    quantity=forms.CharField(label='Quantity',widget=TextInput(attrs={'class': "form-control selectSearch",style:'width: 100%'}))
    unit=forms.ChoiceField(label='Unit',choices=get_unit_choices(), widget=Select(attrs={'class': "form-control"}))
            # 'product': Select(attrs={'class': 'form-control'}),
            # 'quantity': TextInput(attrs={'class': 'form-control'}),
            # 'unit': Select(attrs={'class': 'form-control'},choices=MEDIA_CHOICES),
            # 'recipe': HiddenInput(),
