from django.contrib import admin
from django.urls import path,include
from .views import Userlogin,Userlogout

urlpatterns = [
    path('login/', Userlogin.as_view(), name="login"),
    path('logout/', Userlogout.as_view(), name="logout"),
]