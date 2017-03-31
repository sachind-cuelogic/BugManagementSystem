from django import forms
from .models import User_info
from django.forms import ModelForm
from .models import Product_type
from .models import ProductDetails
from .models import ProductUser

class User_inof_form(ModelForm):
	class Meta:
		model = User_info
		fields = ("username","email","password")

class Product_type_form(ModelForm):
	class Meta:
		model = Product_type
		fields = ('product_type_name',)

class ProductDetailsForm(ModelForm):
	prod_name = forms.CharField(required=True,label="prod_name",
						widget=forms.TextInput(
								attrs={'class':'form-control',
									   'placeholder': 'Enter product name',
									   'required' : 'required'}))

	prod_type = forms.ModelChoiceField(required=True, 
					queryset=Product_type.objects.all(),
						widget=forms.Select(
								attrs={'class':'form-control',
									   'name':'proddrop','label':'Select product type', 'initial':'Select product type'}))

	prod_version = forms.CharField(required=True,label="prod_version",
					widget=forms.TextInput(
							attrs={'class':'form-control',
								   'placeholder': 'Enter product Version',
								   'required' : 'required'}))

	prod_description = forms.CharField(required=True,label="prod_description",
					widget=forms.TextInput(
							attrs={'class':'form-control',
								   'placeholder': 'Enter product Description',
								   'required' : 'required'}))

	prod_file = forms.FileField(
		label='Select a file',
		help_text='max. size 10 MB',widget=forms.FileInput(attrs={'class':'form-control',
					'required' : 'required','name':'prod_file',
					'accept':".jpg, .png, .pdf, .xlsx, .jpeg, .xls, .txt, .doc"}),
		)

	class Meta:
		model = ProductDetails
		fields = ('prod_name','prod_type',
					'prod_version','prod_description','prod_file',)

class ProductUserForm(ModelForm):

	role_choice = (
		(1, ("Software Engineer")),
		(2, ("Tech Lead")),
		(3, ("Project Manager")),
		(4, ("Quality Assurance")),
		(5, ("Tester"))
		)

	prod_user = forms.ModelChoiceField(required=True,
		queryset=User_info.objects.all(),
		widget=forms.Select(
			attrs={'class':'form-control col-md-offset-4',
			}))

	prod_user_role = forms.ChoiceField(choices = role_choice, label="", initial='', 
		widget=forms.Select(attrs={'class':'form-control col-md-offset-8',
			'name':'proddrop2'}), required=True)


	def save(self, commit=True, *args, **kwargs):
		self.instance.product = ProductDetails.objects.get(pk=kwargs.get('args')[0].id)
		self.instance.save()
		print "save me from demo please."

	class Meta:
		model = ProductUser
		fields = ('prod_user','prod_user_role',)
		