from django import forms
from .models import User_info
from django.forms import ModelForm

class User_inof_form(ModelForm):
    class Meta:
        model = User_info
        fields = ("username","email","password")