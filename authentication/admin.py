from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Complaint)
admin.site.register(Contactus)
admin.site.register(SignupFields)