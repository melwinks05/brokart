from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(default=0)
    DELETE = 0
    LIVE = 1
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    DELETE_STATUS = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
