from django.db import models

# Create your models here.
class Destination(models.Model):  
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',default='destination_4.jpg')
    desc = models.TextField(default='Defualt Value')
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)

class UserList(models.Model):
    username = models.CharField(max_length=)
    email = models.EmailField(max_length=254)
    coupon = models.CharField(max_length=100)