from django.urls import path
from .views import store, cart, checkout, search, about, product_detail, update_item, process_order, payment, contact

urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
    path('product-detail/', product_detail, name='product-detail'),
    path('update-cart/', update_item, name='update_item'),
    path('process-order/', process_order, name='process_order'),
    path('payment/', payment, name='payment'),
    path('contact/', contact, name='contact')
]
