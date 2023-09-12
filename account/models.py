from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product_image')
    description=models.CharField(max_length=200)
    options=(
        ('mobile phone','mobile phone'),
        ('earphone','earphone'),
        ('laptop','laptop'),
        ('tablet','tablet'),
        ('smart watch','smart watch'),
        ('BT speaker','BT speaker')
    )
    category=models.CharField(max_length=200,choices=options,default='Mobile phone')

class Cart(models.Model):
    Product=(models.ForeignKey(Product,on_delete=models.CASCADE))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=200,default='cart')
    
   
    @property
    def totalamt(self):
        return self.Product.price*self.quantity


class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE,related_name='cartorders')
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=600,null=True)
    phone=models.IntegerField(null=True)
    options=(
        ('order placed','order placed'),
        ('shipped','shipped'),
        ('out for delivery','out for delivery'),
        ('Delivered','Delivered'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=100,choices=options,default='order placed')