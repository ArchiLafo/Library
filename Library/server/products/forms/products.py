from django import forms
from products.models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'short_description',
            'description',
            'specifications',
            'image',
            'status',
            'file',
        ]