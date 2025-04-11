from django.shortcuts import render
from orders.models import ItemOrdered
from orders.my_forms import OrdersForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrdersForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                ItemOrdered.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    qtd=item['purchase_qtd'],
                )
            
            cart.clean_cart(request)

            return render(request, 'order_complete.html', {'order': order})
    
    else:
        form = OrdersForm()
        return render(request, 'order_create.html', {
            'cart': cart,
            'form': form,
        })