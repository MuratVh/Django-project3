from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/<int:pk>', views.product, name='product'),
    path('guest_register/<int:pk>', views.guest_register, name='guest_register'),
    path('cart/', views.cart, name='cart'),
    path('create_order/', views.create_order, name='create_order'),
    path('favorite/', views.favorite_page, name='favorite'),
    path('orders/', views.orders, name='orders')
]