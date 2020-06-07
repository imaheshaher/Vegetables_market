from django.contrib import admin
from market.models import Vegitables,Seller
from market.models import *
#Register your models here.
admin.site.register(Customer)
admin.site.register(Vegitables)
admin.site.register(Seller)
admin.site.register(Seller_Product)
admin.site.register(Buyer_product)
admin.site.register(User)
