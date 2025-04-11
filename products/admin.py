from django.contrib import admin
from products.models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('model', 'size', 'price', 'stock',)
    search_fields = ('model', 'size', 'price',)
    list_filter = ('model', 'size', 'price', 'stock',)

admin.site.register(Products, ProductsAdmin)