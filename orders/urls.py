from django.urls import path, include
from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_create, name='order_create'),

    path('paypal/', include('paypal.standard.ipn.urls')),

    path('payment_success/', views.payment_success, name='payment_success'),

    path('payment_failed/', views.payment_failed, name='payment_failed'),
]