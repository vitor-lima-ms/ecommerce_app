from django.shortcuts import render
from orders.models import ItemOrdered
from orders.my_forms import OrdersForm
from cart.cart import Cart
# PayPal
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

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

            # PayPal
            host = request.get_host()
            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount': cart.get_grand_total(),
                'item_name': 'Pedido',
                'no_shipping': '2',
                'invoice': str(uuid.uuid4()),
                'currency_code': 'BRL',
                'notify_url': 'https://{}{}'.format(host, reverse('orders:paypal-ipn')),
                'return_url': 'https://{}{}'.format(host, reverse('orders:payment_success')),
                'cancel_return': 'https://{}{}'.format(host, reverse('orders:payment_failed')),
            }

            paypal_form = PayPalPaymentsForm(initial=paypal_dict)
            context = {
                'form': paypal_form,
                'order': order,
            }
            
            cart.clean_cart(request)

            return render(request, 'order_complete.html', context)
    
    else:
        form = OrdersForm()
        return render(request, 'order_create.html', {
            'cart': cart,
            'form': form,
        })

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')