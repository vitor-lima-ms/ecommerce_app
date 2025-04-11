from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('product_details/<int:id>', views.product_details, name='product_details'),
]