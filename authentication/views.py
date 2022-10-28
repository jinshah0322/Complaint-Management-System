from audioop import add
from email.message import EmailMessage
from tokenize import generate_tokens
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from cms import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from cms.tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .forms import *

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        Name=request.POST['Name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if User.objects.filter(username=Name):
            messages.error(request,"Username already exists",extra_tags="validation")
            return redirect('/signup')

        if User.objects.filter(email=email):
            messages.error(request,"Email already exists",extra_tags="validation")
            return redirect('/signup')

        if password != confirm_password:
            messages.error(request,"Password does not match",extra_tags="validation")
            return redirect('/signup')

        if not Name.isalnum():
            messages.error(request,"Username should only contain letters and numbers",extra_tags="validation")
            return redirect('/signup')

        myuser=User.objects.create_user(Name, email, password)
        myuser.first_name=Name  
        myuser.email=email
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Your account has been successfully created Check mail to verify.",extra_tags="valid")

        #welcome email
        subject = "Welcome to Complaint Management System"
        message = "Hi "+myuser.first_name+"! Welcome to Complaint Management System!!!.\n We are glad to have you here!!!.\nWe have sent you a confirmation email to "+myuser.email+".\nPlease confirm your email to continue using our services.\n\nThank You!!!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        #confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirm your email"
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently = True
        email.send()

        return redirect('/')

    return render(request,"authentication/signup.html")

def signin(request):
    if(request.method=="POST"):
        Name=request.POST['Name']
        password=request.POST['Password']
        user=authenticate(username=Name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            validate = User.objects.filter(username=Name).exists()  
            if validate:
                messages.error(request,"Invalid Password",extra_tags="pass")
                return redirect('/')
            else:
                messages.error(request,"Invalid Username",extra_tags="user")
                return redirect('/')
    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"You have been successfully logged out",extra_tags="logout")
    return redirect('/')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('/home')
    else:
        return render(request, 'activation_failed.html')

def complaint(request):
    form = ComplaintForm()
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,"Your complaint has been successfully registered",extra_tags="valid")
            return redirect('/complaint')
    context={'form':form}
    return render(request,"authentication/complaint.html",context)

def contactus(request):
    form = ContactusForm()
    if request.method == "POST":
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,"Your message has been successfully sent",extra_tags="valid")
            return redirect('/contactus')
    context = {'form':form}
    return render(request,"authentication/contactus.html",context)

def account(request):
    return render(request,"authentication/account.html")