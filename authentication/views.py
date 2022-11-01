from audioop import add
from curses import use_default_colors
import email
from email.message import EmailMessage
from tokenize import generate_tokens
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from cms import settings
from authentication.models import Complaint
from authentication.models import Contactus
from django.contrib.auth import get_user_model
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


def signup(request):
     if request.method == "POST":
            name=request.POST.get('Name')
            number=request.POST.get('number')
            email=request.POST.get('email')
            address=request.POST.get('address')
            age=request.POST.get('age')
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if User.objects.filter(name=name):
                messages.error(request,"Username already exists",extra_tags="validation")
                return redirect('/signup')

            if User.objects.filter(mail=email):
                messages.error(request,"Email already exists",extra_tags="validation")
                return redirect('/signup')

            if password != confirm_password:
                messages.error(request,"Password does not match",extra_tags="validation")
                return redirect('/signup')

            if not name.isalnum():
                messages.error(request,"Username should only contain letters and numbers",extra_tags="validation")
                return redirect('/signup')
                
            data=User(name=name,password=password,mail=email,number=number,address=address,age=age)
            data.save()
            messages.success(request,"Your account has been successfully created Check mail to verify.",extra_tags="valid")
            #welcome email
            subject = "Welcome to Complaint Management System"
            message = "Hi "+data.name+"! Welcome to Complaint Management System!!!.\n We are glad to have you here!!!.\nWe have sent you a confirmation email to "+data.mail+".\nPlease confirm your email to continue using our services.\n\nThank You!!!"
            from_email = settings.EMAIL_HOST_USER
            to_list = [data.mail]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            # #confirmation email
            current_site = get_current_site(request)
            email_subject = "Confirm your email"
            message2 = render_to_string('email_confirmation.html', {
                'name': data.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(data.pk)),
                'token': generate_token.make_token(data)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [data.email]
            )
            email.fail_silently = True
            email.send()

            return redirect('/')

     return render(request,"authentication/signup.html")

def signin(request):
    if(request.method=="POST"):
        Name=request.POST['Name']
        password=request.POST['Password']
        if Name=='admin' and password=='123':
            return redirect('/admins')

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

def home(request):
    return render(request,"authentication/index.html") 
    
    
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
   


def dashboard(request):
    context={}
    context["Water"]=Complaint.objects.filter(name=request.user,cname='Water').count()
    context["Light"]=Complaint.objects.filter(name=request.user,cname='Light').count()
    context["Clean"]=Complaint.objects.filter(name=request.user,cname='Clean').count()
    context["Other"]=Complaint.objects.filter(name=request.user,cname='Other').count()
    return render(request,"authentication/dashboard.html",context)
   

    
def dashboard_water(request):
    context={}
    context["Complaints"]=Complaint.objects.filter(name=request.user,cname='Water')     
    return render(request,"authentication/dashboard_topic.html",context)

def dashboard_light(request):
    context={}
    context["Complaints"]=Complaint.objects.filter(name=request.user,cname='Light')        
    return render(request,"authentication/dashboard_topic.html",context)

def dashboard_clean(request):
    context={}
    context["Complaints"]=Complaint.objects.filter(name=request.user,cname='Clean')    
    return render(request,"authentication/dashboard_topic.html",context)

def dashboard_other(request):
    context={}
    context["Complaints"]=Complaint.objects.filter(name=request.user,cname='Other')    
    return render(request,"authentication/dashboard_topic.html",context)


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
        if request.user.is_authenticated:
            return render(request,"authentication/account.html")
        else:
            return redirect('/')        
    

def form(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('mail')
        number=request.POST.get('number')
        message=request.POST.get('message')
        data=Contactus(name=name,number=number,mail=email,message=message)
        data.save()
    return render(request,"authentication/index.html")

def complaintform(request):
    if request.method == "POST":
            name=request.user
            cname=request.POST.get('cname')
            desc=request.POST.get('cdesc')
            priority=request.POST.get('priority')
            date=request.POST.get('date')
            data=Complaint(name=name,cname=cname,cdescription=desc,priority=priority,date=date)
            data.save()
    return render(request,"authentication/index.html")    

def admin(request):
    context={}
    context["Complaints"]=Complaint.objects.filter(status="In Process")    
    context["Users"]=User.objects.filter().count()-1
    context["Total_Complaints"]=Complaint.objects.filter().count()  
    context["Total_Completed_Complaints"]=Complaint.objects.filter(status="Accepted").count() + Complaint.objects.filter(status="Rejected").count() 
    context["Remaining_Complaints"]=Complaint.objects.filter().count()-Complaint.objects.filter(status="Rejected").count()-Complaint.objects.filter(status="Accepted").count() 
    return render(request,"authentication/admin.html",context)

def yes(request,pk):
    t = Complaint.objects.get(id=pk)
    t.status = 'Accepted' 
    t.save()
    return redirect("/admins") 

def no(request,pk):
    t = Complaint.objects.get(id=pk)
    t.status = 'Rejected' 
    t.save()
    return redirect("/admins") 

def query(request):
    context={}
    context["Contactus"]=Contactus.objects.all()    
    return render(request,"authentication/query.html",context)

def oldcomplaints(request):
    context={}
    context["Complaints_Old"]=Complaint.objects.filter(status="Accepted") | Complaint.objects.filter(status="Rejected")        
    return render(request,"authentication/old_complaints.html",context)
