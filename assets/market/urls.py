from django.urls import path
from . import views

urlpatterns =[
    path('',views.welcome,name='welcome'),
    path('home',views.home,name='home'),
    path('login',views.login,name="login")
  ]