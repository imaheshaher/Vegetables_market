from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()

class UserForm(forms.ModelForm):
  class Meta:
    model=User
    fields=['username','first_name','last_name','password']


class CustomerForm(forms.ModelForm):
  class Meta:
    model=Customer
    exclude=['user']
    fields=['mob_no','address']
class SellerForm(forms.ModelForm):
  
  class Meta:
    
    model=Seller
    exclude=['user']
    fields=['mob_no','shop_name','address']
    
class SProductForm(forms.ModelForm):
  class Meta:
    model=Seller_Product
    #exclude=['sid']
    fields=['veg_id','price','quantity']
    
class BuyProductForm(forms.ModelForm):
  class Meta:
    model=Buyer_product
    fields=['quantity']