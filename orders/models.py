from django.db import models
from decimal import Decimal
from products.models import Products

# Create your models here.

class Orders(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created']

    def __str__(self):
        return f'Order #{self.id}'
    
    def get_grand_total(self):
        result = Decimal (0.0)

        for item in self.items.all():
            subtotal = Decimal(item['purchased_qtd']) * Decimal(item['price'])
            result += subtotal
        
        return result
        
class ItemOrdered(models.Model):
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='ordered_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qtd = models.PositiveIntegerField(default=1)

    def get_subtotal(self):
        return self.price * self.qtd