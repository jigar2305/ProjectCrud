from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class Userlogin(LoginView):
    template_name = "core/login.html"

class Userlogout(LogoutView):
    pass
    