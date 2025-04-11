from django.contrib import admin
from orders.models import ItemOrdered, Orders

# Register your models here.

class ItemOrderedInline(admin.TabularInline):
    model = ItemOrdered
    raw_id_fields = ['product']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'address',
        'postal_code',
        'city',
        'paid',
        'created',
    ]
    list_filter = ['paid', 'created', 'name']

    inlines = [ItemOrderedInline]