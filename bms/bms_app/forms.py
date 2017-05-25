from django import forms
from django.forms import ModelForm
from .models import ProductDetails
from .models import ProductUser
from .models import BugType
from .models import BugStatus
from .models import BugDetails, Comments
from django.contrib.auth.models import User

class User_info_form(ModelForm):
	class Meta:
		model = User
		fields = ("username","email","password")

class Bug_Details_Form(forms.ModelForm):
	
	class Meta:
		model = BugDetails
		fields = ('project_name','title','bug_type','status',
					'bug_owner','bug_assigned_to',)
		
class comment_form(ModelForm):
	class Meta:
		model = Comments
		fields = ('user','bug','comment',)
		