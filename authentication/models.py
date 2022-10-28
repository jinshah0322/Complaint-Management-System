from django.db import models 
from django.contrib.auth.models import User
from cms import settings

# Create your models here.
class Complaint(models.Model):
    complaint_name = models.CharField(max_length=100)
    complaint_description = models.TextField()
    CHOICES=[('High','High'),('Moderate','Moderate'),('Low','Low')]
    priority = models.CharField(max_length=10,choices=CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.complaint_name,self.complaint_description,self.priority,self.date

class Contactus(models.Model):
    name = models.CharField(max_length=100,null=True)
    phoneNumber = models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length = 254,null=True)
    message = models.TextField(null=True)
    date_of_register = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name,self.phoneNumber,self.email,self.message,self.date_of_register