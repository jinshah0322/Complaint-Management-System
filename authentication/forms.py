from django.forms import ModelForm
from .models import *

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'

class ContactusForm(ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'