from django import forms
from django.forms import ModelForm
from .models import Product_type
from .models import ProductDetails
from .models import ProductUser
from .models import BugType
from .models import BugStatus
from .models import Bug_Details
from django.contrib.auth.models import User

class User_info_form(ModelForm):
	class Meta:
		model = User
		fields = ("username","email","password")

class Bug_Details_Form(forms.ModelForm):
	project_name = forms.ModelChoiceField(required=True, 
								queryset=ProductDetails.objects.all(),
								empty_label='Select project name',
								widget=forms.Select(
								attrs={'class':'form-control',
								'name':'project_name'}))

	title = forms.CharField(required=True,label="bug_title",
								widget=forms.TextInput(
								attrs={'class':'form-control',
									   'placeholder': 'Enter bug title',
									   'required' : 'required'}))


	bug_type = forms.ModelChoiceField(required=True, 
								queryset=BugType.objects.all(),
								empty_label='Select bug type',
								widget=forms.Select(
								attrs={'class':'form-control',
								'name':'bug_type'}))

	status = forms.ModelChoiceField(required=True, 
								queryset=BugStatus.objects.all(),
								empty_label='Select bug status',
								widget=forms.Select(
								attrs={'class':'form-control',
								'name':'bug_status'}))

	build_version = forms.CharField(required=False,
								label="build_version",
								widget=forms.TextInput(
								attrs={'class':'form-control',
									   'placeholder': 'Enter Build Version No.'}))

	sprint_no = forms.CharField(required=False,
								label="sprint_no",
								widget=forms.TextInput(
								attrs={'class':'form-control',
									   'placeholder': 'Enter Sprint No.'}))

	dependent_module = forms.CharField(required=False,
								label="dependent_module",
								widget=forms.TextInput(
								attrs={'class':'form-control',
									   'placeholder': 'Enter dependent module'}))

	description = forms.CharField(required=False,
								label="bug_description",
								widget=forms.TextInput(
								attrs={'class':'form-control',
								   'placeholder': 'Enter Bug Description'}))

	bug_owner = forms.ModelChoiceField(required=True, 
								queryset=User.objects.all(),
								empty_label='Select bug owner',
								widget=forms.Select(
								attrs={'class':'form-control',
								'name':'bug_owner'}))

	bug_assigned_to = forms.ModelChoiceField(
								queryset=User.objects.all(),
								empty_label='Select user to assign bug',
								widget=forms.Select(
								attrs={'class':'form-control',
								'name':'bug_assigned_to'}))

	bug_file = forms.FileField(required=False,
				label='Select a file',
				help_text='max. size 10 MB',
				widget=forms.FileInput(attrs={'class':'form-control',
				'name':'bug_file',
				'accept':".jpg, .png, .pdf, .xlsx, .jpeg, .xls, .txt, .doc"}),)

	class Meta:
		model = Bug_Details
		fields = ('project_name','title','bug_type','status',
					'build_version','sprint_no','dependent_module','description',
					'bug_owner','bug_assigned_to','bug_file')
