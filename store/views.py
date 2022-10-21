from math import prod
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from store.utils import cookieCart, cartData, guestOrder
from .models import *


# Create your views here.
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems
    }
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        'items': items,
        'order': order, 
        'cartItems': cartItems
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems
    }
    return render(request, 'store/checkout.html', context)


def  update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ', action)
    print('Product: ', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
 
 
def process_order(request):
    print('Data: ', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
        
        
    else:
        customer, order = guestOrder(request, data)
    
    total = int(data['form']['total'])
    order.transaction_id = transaction_id
        
    if total == order.get_cart_total:
        order.complete = True
    order.save()
    
    ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address2=data['shipping']['address2'],
            city=data['shipping']['city'],
            state=data['shipping']['state']

        )
    return JsonResponse('Address Info Saved', safe=False)


def payment(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems
    }
    return render(request, 'store/payment.html', context)


def about(request):
    context = {
        
    }
    return render(request, 'store/about.html', context)


def search(request):
    context = {
        
    }
    return render(request, 'store/search.html', context)


def product_detail(request):
    context = {
        
    }
    return render(request, 'store/product-detail.html', context)

def contact(request):
    context = {
        
    }
    return render(request, 'store/contact.html', context)