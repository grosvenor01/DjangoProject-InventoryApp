from socket import fromshare
from django import forms
from .models import *
class formProduct(forms.ModelForm):
    class Meta():
        model=product
        fields=[
            'id',
            'product',
            'category',
            'quantité',
        ]