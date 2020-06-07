from django.db import models
from django.contrib.auth.models import  AbstractUser,User
from Veg import settings
# Create your models here.
from django.contrib.auth import get_user_model
from Veg import settings

class User(AbstractUser):
  @property
  def is_customer(self):
    if hasattr(self,'customer'):
      return True
    return False
    
  @property
  def is_seller(self):
    if hasattr(self,'seller'):
      return True
      
    return False
class Customer(models.Model):
  user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  mob_no=models.IntegerField()
  address=models.CharField(max_length=100)
  
  def __str__(self):
    return str(self.user)

class Vegitables(models.Model):
  veg_name=models.CharField(max_length=100)
  veg_img=models.ImageField(upload_to='images/')  
  
  def __str__(self):
    return str(self.veg_name)
  
class Seller(models.Model):
  user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  mob_no=models.IntegerField()
  shop_name=models.CharField(max_length=100)
  address=models.CharField(max_length=100)
  
  def __str__(self):
    return str(self.user)

class Seller_Product(models.Model):
  sid=models.ForeignKey(Seller,on_delete=models.CASCADE)
  veg_id=models.ForeignKey(Vegitables,on_delete=models.CASCADE)
  price=models.IntegerField()
  quantity=models.IntegerField()
  
  def __str__(self):
    return str(self.sid)
class Buyer_product(models.Model):
  cid=models.ForeignKey(Customer,on_delete=models.CASCADE)
  sid=models.ForeignKey(Seller,on_delete=models.CASCADE)
  veg_id=models.ForeignKey(Vegitables,on_delete=models.CASCADE)
  quantity=models.IntegerField()
  total_price=models.IntegerField()
  
  def __str__(self):
    return "{} {}".format(self.cid,self.sid)
  
  