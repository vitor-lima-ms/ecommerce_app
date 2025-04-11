from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart_summary', views.cart_summary, name='cart_summary'),

    path('cart_add/<int:id>', views.cart_add, name='cart_add'),
    
    path('cart_delete/<int:id>/<int:purchase_qtd>', views.cart_delete , name='cart_delete'),
]