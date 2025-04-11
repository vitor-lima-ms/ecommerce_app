from django import forms
from orders.models import Orders

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'