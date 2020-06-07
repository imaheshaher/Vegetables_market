from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('register_seller',views.register_seller,name='register_seller'),
    path('home',views.home,name='home'),
    path('welcome',views.welcome,name='welcome'),
    path('seller_product/<slug:sid>',views.seller_product,name="seller_product"),
    path('logout',views.logout,name='logout'),
    path('all_data',views.all_data,name='alldata'),
    path('buy_product/<id>',views.buy_product,name='buy_product'),
    path('check_product/<sid>',views.check_product,name="check_product")
    #path('product_info',views.product_info,name='product_info')
    
    
  ]
  
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)