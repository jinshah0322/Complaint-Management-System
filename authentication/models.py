from email.policy import default
from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_name = models.CharField(max_length=100)
    complaint_description = models.TextField()
    CHOICES=[('High','High'),('Moderate','Moderate'),('Low','Low')]
    priority = models.CharField(max_length=10,choices=CHOICES)
    date = models.DateField(auto_now_add=True)

class Contactus(models.Model):
    name = models.CharField(max_length=100,null=True)
    phoneNumber = models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length = 254,null=True)
    message = models.TextField(null=True)
    date_of_register = models.DateField(auto_now_add=True,null=True)