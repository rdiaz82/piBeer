from django.forms import ModelForm, TextInput, Select, Textarea
from recipeManager.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'product_type': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control','col':3,'row':3}),
        }
