from django.shortcuts import render, get_object_or_404
from products.models import Products
from cart.my_forms import AddCartForm

# Create your views here.

def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    form = AddCartForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'product_details.html', context,)