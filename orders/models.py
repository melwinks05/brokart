from django.db import models
from customers.models import Customer
from products.models import Products

# Create your models here.
class Order(models.Model):
  DELETE = 0
  LIVE = 1
  DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))

  CART_STAGE = 0
  ORDER_CONFIRMED = 1
  ORDER_PROCESSED = 2
  ORDER_DELIVERED = 3
  ORDER_REJECTED = 4
  STATUS_CHOICES = (
    (CART_STAGE, 'Cart'),
    (ORDER_PROCESSED, 'Order Processed'),
    (ORDER_DELIVERED, 'Order Delivered'),
    (ORDER_REJECTED, 'Order Rejected'),
  )

  order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
  total_price = models.FloatField(default=0)
  owner = models.ForeignKey(Customer, related_name='orders', on_delete=models.SET_NULL, null=True)
  delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return "Order-{}-{}".format(self.id, self.owner.name)


class OrderedItem(models.Model):
  product = models.ForeignKey(Products, related_name='cart_items', on_delete=models.SET_NULL, null=True)
  owner = models.ForeignKey(Order, related_name='added_items', on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)