from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('ip_address', 'info', 'hostname', 'able_to_ping', 'able_to_login',
                  'physical_or_vm', 'issues')
