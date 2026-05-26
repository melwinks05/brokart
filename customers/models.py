from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    DELETE = 0
    LIVE = 1
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    DELETE_STATUS = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name='customer_profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username