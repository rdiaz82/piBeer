from django.forms import ModelForm, TextInput, Select, Textarea
from recipeManager.models import Product
from recipeManager.models import ProductType
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'product_type': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control','col':3,'row':3}),
        }

class ProductFilterForm(forms.Form):
    name=forms.CharField(max_length=50,required=False, widget=forms.TextInput(attrs={'class': "form-control col-lg-3"}))
    product_type=forms.ModelChoiceField(queryset=ProductType.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control col-lg-3'}))
