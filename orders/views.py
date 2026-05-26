from django.shortcuts import render, redirect
from . models import Order, OrderedItem
from products.models import Products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='account')
def show_cart(request):
  user=request.user
  customer=user.customer_profile
  cart_obj, created=Order.objects.get_or_create(
    owner=customer, 
    order_status=Order.CART_STAGE
  )
  context={'cart':cart_obj}
  return render(request, 'cart.html', context)

def remove_from_cart(request, pk):
  item=OrderedItem.objects.get(pk=pk)
  if item:
    item.delete()
  return redirect('cart')

@login_required(login_url='account')
def show_orders(request):
  user=request.user
  customer=user.customer_profile
  all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
  context={'orders':all_orders}
  return render(request, 'orders.html', context)

@login_required(login_url='account')
def add_to_cart(request):
  if request.POST:
    user=request.user
    customer=user.customer_profile
    quantity=int(request.POST.get('quantity', 1))
    product_id=request.POST.get('product_id')
    cart_obj,created=Order.objects.get_or_create(
      owner=customer, 
      order_status=Order.CART_STAGE
    )
    product = Products.objects.get(pk=product_id) 
    ordered_item, created = OrderedItem.objects.get_or_create(
      product=product,
      owner=cart_obj,
    )
    if created:
      ordered_item.quantity=quantity
      ordered_item.save()
    else:
        ordered_item.quantity += quantity
        ordered_item.save()
    return redirect('cart')
  
def checkout_cart(request):
  if request.POST:
    try:
      user=request.user
      customer=user.customer_profile
      total_raw = request.POST.get('total', 0)
      total=float(total_raw)
      order_obj=Order.objects.get(
        owner=customer, 
        order_status=Order.CART_STAGE
      )
      if order_obj:
        order_obj.order_status=Order.ORDER_CONFIRMED
        order_obj.total_price=total
        order_obj.save()
        status_maessage='Your order has been placed successfully'
        messages.success(request, status_maessage)
      else:
        status_maessage='Your order could not be placed'
        messages.error(request, status_maessage)
    except Exception as e:
      status_maessage='Your order could not be placed'
      messages.error(request, status_maessage)
    return redirect('cart')