from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("login",views.loginUser,name='login'),
    path("SignUp",views.SignUp,name='SignUp'),
    path("logout",views.logoutUser,name="logout"),
    path("submit_contact",views.contact,name='contact'),
    path("userpanel",views.userpanel,name="userpanel"),
     path("CodePost",views.CodePost,name="CodePost"),
      path("Events",views.Events,name="Events"),
       path("Setting",views.Setting,name="Setting")
    ]
