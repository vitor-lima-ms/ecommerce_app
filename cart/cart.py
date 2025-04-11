from decimal import Decimal
from django.conf import settings
from products.models import Products

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.ID_SHOPPING_CART)

        if not cart:
            cart = self.session[settings.ID_SHOPPING_CART] = {}
        
        self.cart = cart
    
    def save(self):
        self.session[settings.ID_SHOPPING_CART] = self.cart
        self.session.modified = True
    
    def add(self, product, qtd=1, att_qtd=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'purchase_qtd': 0,
                'price': str(product.price),
            }
        
        if att_qtd:
            self.cart[product_id]['purchase_qtd'] = qtd
        else:
            self.cart[product_id]['purchase_qtd'] += qtd
        
        self.save()
    
    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.save()
    
    def __iter__(self):
        products_ids = self.cart.keys()
        products = Products.objects.filter(id__in=products_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['subtotal'] = Decimal(item['price']) * Decimal(item['purchase_qtd'])
            yield item
    
    def len(self):
        result = Decimal(0.0)
        for item in self.cart.values():
            result += item['purchase_qtd']
        
        return result

    def get_grand_total(self):
        result = Decimal(0.0)
        for item in self.cart.values():
            subtotal = Decimal(item['price']) * Decimal(item['purchase_qtd'])
            result += subtotal
        
        return result
    
    def clean_cart(self, request):
        for key in list(request.session.keys()):
            del request.session[key]
        request.session.modified = True