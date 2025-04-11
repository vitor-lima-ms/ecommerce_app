from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Products
from cart.cart import Cart
from cart.my_forms import AddCartForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

def cart_summary(request):
    cart = Cart(request)
    for item in cart:
        item['shop_cart_form'] = AddCartForm(initial={
            'qtd': item['purchase_qtd'],
            'att': True,
        })
    
    cart_len = True if cart.len() > 0 else False

    context = {
        'cart': cart,
        'cart_len': cart_len,
    }
    
    return render(request, 'cart_summary.html', context)

@require_POST
@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=id)
    form = AddCartForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data

        if data['qtd'] > product.stock:
            messages.error(request, 'Quantidade requerida maior do que a em estoque!')
            form = AddCartForm()
            context = {
                'product': product,
                'form': form,
            }
            return render(request, 'product_details.html', context)
        else:
            cart.add(product, qtd=data['qtd'], att_qtd=data['att'])
            product.stock -= data['qtd']
            product.save()
    
    return redirect('cart:cart_summary')


def cart_delete(request, id, purchase_qtd):
    cart = Cart(request)
    product = get_object_or_404(Products, id=id)
    cart.remove(product)

    product.stock += purchase_qtd
    print(product.stock)
    product.save()

    return redirect('cart:cart_summary')