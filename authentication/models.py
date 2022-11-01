from ast import Pass
from mailbox import Mailbox
from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models 
from django.contrib.auth.models import User
from cms import settings

# Create your models here.

class Complaint(models.Model):
    name = models.CharField(max_length=100,null=True)
    cname = models.CharField(max_length=100)
    cdescription = models.TextField()
    CHOICES=[('High','High'),('Moderate','Moderate'),('Low','Low')]
    priority = models.CharField(max_length=10,choices=CHOICES)
    date = models.DateField(auto_now_add=True)
    status=models.CharField(default='In Process',max_length=10)

    def __str__(self):
        return  self.name,self.cname,self.cdescription,self.priority,self.status

class Contactus(models.Model):
    name = models.CharField(max_length=100,null=True)
    number = models.CharField(max_length=10,null=True)
    mail = models.EmailField(max_length = 254,null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name,self.number,self.mail,self.message