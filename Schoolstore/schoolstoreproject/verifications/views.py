from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        pswd=request.POST['password']
        cpswd=request.POST['confirm_password']

        if pswd==cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already exists")
            else:
                user=User.objects.create_user(username=uname,password=pswd)
                user.save()
                print("User Created")
                return redirect("verifications:login")
        else:
            messages.info(request,"Password doesn't match")


    return render(request,"register.html")


def login(request):
    if request.method=='POST':
        uname2=request.POST['username']
        pswd2=request.POST['password']
        user=auth.authenticate(username=uname2,password=pswd2)

        if user is not None:
            auth.login(request,user)
            return redirect("verifications:detail")
        else:
            messages.info(request, "Invalid Credentials...")


    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def detail(request):
    return render(request,"detail.html")

def form(request):
    return render(request,"form.html")







