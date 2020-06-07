from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import get_user_model
User=get_user_model()
@login_required  
def home(request):
  if request.user.is_seller:
    seller="user is seller"
    seller_data=Seller.objects.get(user=request.user)
    
    product_data=Seller_Product.objects.all().filter(sid_id=seller_data.user.id)
    print(product_data)
    return render(request,'profile.html',{'seller_data':seller_data,'product_data':product_data})
  if request.user.is_customer:
    #images=[]
    #all_product=Seller_Product.objects.all()
    #for image in all_product:
      #i=Vegitables.objects.filter(veg_name=image.veg_id)
      #images.append(i.veg_img)
      
    return redirect('alldata')
  return render(request,'home.html')


def register(request):
  if request.method=='POST':
    form=UserForm(request.POST)
    form1=CustomerForm(request.POST)
    if form.is_valid() and form1.is_valid():
      userform=form.save(commit=False)
      password=request.POST['password']
      userform.set_password(password)
      userform.save()
      custform=form1.save(commit=False)
      custform.user=userform
      custform.save()
      
      return redirect ('home')
      
  else:
    form=UserForm()
    form1=CustomerForm()
      
      
  return render(request,"register1.html")

'''@login_required
def login(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      if user.is_seller:
        return HttpResponse("{} seller is login succesfully".format(username))
      if user.is_customer:
        return HttpResponse("user is customer")
  return render(request,'index.html')
  
'''
def register_seller(request):
  if request.method=='POST':
    form=UserForm(request.POST)
    form1=SellerForm(request.POST)
    if form.is_valid() and form1.is_valid():
      userform=form.save(commit=False)
      password=request.POST['password']
      userform.set_password(password)
      userform.save()
      sellerform=form1.save(commit=False)
      sellerform.user=userform
      sellerform.save()
      return redirect('home')
      
    
  else:
    form=UserForm()
    form1=SellerForm
    
  return render(request,"register_seller.html")
  
def welcome(request):
  seller_data=Seller_Product.objects.all()
  list1=[]
  for vegdata in seller_data:
    veg=Vegitables.objects.get(veg_name=vegdata.veg_id)
    print(veg.veg_img)
    list1.append(veg.veg_img)
  print(list1)
  mylist=seller_data

  return render(request,'welcome.html',{'mylist': mylist,'list1':list1})
@login_required()  
def seller_product(request,sid):
  all_veg=Vegitables.objects.all()
  sellerid=Seller.objects.get(user=request.user)
  #print(sellerid)
  #print(sid)
  if request.method=='POST':
    form=SProductForm(request.POST)
    if form.is_valid():
      #print('form is valid')
      #print(request.user.id)
      #print(sellerid)
      spform=form.save(commit=False)
      spform.sid=sellerid
      spform.save()
      return redirect('home')
  else:
    form=SProductForm()
  return render(request,'seller_product.html',{'form':form})
      
      
  
def logout(request):
  auth.logout(request)
  return redirect('welcome')
  
  
@login_required()  
def all_data(request):
  seller_data=Seller_Product.objects.all()
  list1=[]
  for vegdata in seller_data:
    veg=Vegitables.objects.get(veg_name=vegdata.veg_id)
    print(veg.veg_img)
    list1.append(veg.veg_img)
  print(list1)
  mylist=seller_data

  return render(request,'all_data.html',{'mylist': mylist,'list1':list1})
  
@login_required()  
def buy_product(request,id):
  
  print(id)
  if request.method=='POST':
    form=BuyProductForm(request.POST)
    customerid=Customer.objects.get(user=request.user.id)
    if form.is_valid():
      print(id)
      buyform=form.save(commit=False)
      data=Seller_Product.objects.get(id=id)
      sellerid=Seller.objects.get(id=data.sid_id)
      vegid=Vegitables.objects.get(id=data.veg_id_id)
      buyform.cid=customerid
      buyform.sid=sellerid
      buyform.veg_id=vegid
      buyform.total_price=int(request.POST['quantity'])*int(data.price)
      buyform.save()
      price=buyform.total_price
      return render(request,'product_info.html',{'price':price})
  else:
    form=BuyProductForm()
      
  
  
  return render(request,'buy_product.html',{'id':id,'form':form})
  
def check_product(request,sid):
  data=Seller_Product.objects.all().filter(sid_id=request.user.id)

  return render(request,'check_product.html',{'data':data})