from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Register,name="register"),
   path("adduser",views.AddUser,name="adduser"),
   path("loginuser",views.Loginuser,name="loginuser"),  
]

