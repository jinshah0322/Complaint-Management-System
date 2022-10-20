from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        Name=request.POST['Name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        myuser=User.objects.create_user(Name, email, password)
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/signin')
    return render(request,"authentication/signup.html")

def signin(request):
    if(request.method=="POST"):
        Name=request.POST['Name']
        password=request.POST['Password']
        user=authenticate(username=Name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/signin')
    return render(request,"authentication/signin.html")

def signout(request):
    pass