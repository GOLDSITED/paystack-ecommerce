from django import forms
from .models import ReviewRating

from django.forms import ModelForm, Textarea
from django import forms
from . models import Product



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','product_name','slug','description','price','old_price', 'is_available','image','stock']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'old_price': forms.TextInput(attrs={'class': 'form-control'}),
            'is_available': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Reviewform(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
