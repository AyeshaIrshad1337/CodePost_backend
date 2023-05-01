from django.shortcuts import render, HttpResponse 
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request,"index.html")
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("pswd")
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect("/userpanel")
        else:
            return render(request,"Login_SignUp.html")
    return render(request,"Login_SignUp.html")
def logoutUser(request):
    logout(request)
    return redirect("/login")
def SignUp(request):
    return render(request,"Login_SignUp.html")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact =Contact(name=name,email=email,message=message,date=datetime.today())
        contact.save()  
        messages.success(request, "Your message has been sent.")    
    return render(request,"index.html")
def userpanel(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request,"userpanel.html")
def CodePost(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request,"CodePost.html")
def Setting(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request,"Setting.html")
def Events(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request,"Events.html")