from django.shortcuts import render, get_object_or_404
from products.models import Products

# Create your views here.

def index(request):
    products = Products.objects.all().filter(stock__gt=0).order_by('size')
    return render(request, 'index.html', {
        'products': products,
    })