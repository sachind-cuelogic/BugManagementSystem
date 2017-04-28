from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate
from django.test import RequestFactory
from .views import login, register, create_bug
import json
import os
from .models import BugDetails, ProductDetails, BugType, BugStatus, ProjectType
from .forms import User_info_form, Bug_Details_Form
from django.core.files import File

class SimpleTest(TestCase):

	# def test_register(self):
	# 	client = Client()
	# 	response = self.client.post(reverse('register'),
	# 								{'username':os.environ.get('reg_uname'),
	# 								'email':os.environ.get('reg_email'),
	# 								'password':os.environ.get('reg_pass')})
	# 	print response
	# 	self.assertTrue(response.status_code,200)


	# def test_user_form(self):
	# 	data = {'username':os.environ.get('uform_uname'),
	# 			'email':os.environ.get('uform_email'),
	# 			'password':os.environ.get('uform_pass')}
	# 	form = User_info_form(data=data)
	# 	self.assertTrue(form.is_valid())


	# def test_user_form_fail(self):
	# 	user =User.objects.create(username=os.environ.get('uform_f_uname'), password='')
	# 	data = {'username': user.username, 'password': user.password,}
	# 	form = User_info_form(data=data)
	# 	self.assertFalse(form.is_valid())


	# def test_login(self):
	# 	client = Client()
	# 	response = client.post(reverse('register'),
	# 								{'username':os.environ.get('reg_uname'),
	# 								'email':os.environ.get('reg_email'),
	# 								'password':os.environ.get('reg_pass')})
	# 	response = client.post(reverse('login'),
	# 								{'username':os.environ.get('reg_uname'),
	# 								'password':os.environ.get('reg_pass')})
	# 	print response
	# 	self.assertTrue(response.status_code,200)

	# def test_login_fail(self):
	# 	client = Client()
	# 	response = client.post(reverse('register'),
	# 								{'username':os.environ.get('logf_uname'),
	# 								'email':os.environ.get('logf_email'),
	# 								'password':os.environ.get('logf_pass')})
	# 	response = client.post(reverse('login'),
	# 								{'username':os.environ.get('logf_uname1'),
	# 								'password':os.environ.get('logf_pass1')})
	# 	print response
	# 	self.assertTrue(response.status_code,200)


	# def test_register_fail(self):
	# 	user = User.objects.create_user({'username':os.environ.get('log_uname'),
	# 								'email':os.environ.get('log_email'),
	# 								'password':os.environ.get('log_pass')})
	# 	user.save()
	# 	client = Client()
	# 	response = self.client.post(reverse('register'),
	# 							{'username':os.environ.get('regf_uname'),
	# 							'password':os.environ.get('regf_pass')})
	# 	self.assertTrue(response.status_code,200)


	# def test_landing_page(self):
	# 	resp = self.client.get('/')
	# 	self.assertEqual(resp.status_code, 200)

	# def test_website_home(self):
	# 	resp = self.client.get('/website_home/')
	# 	self.assertEqual(resp.status_code, 200)

	# def test_services(self):
	# 	resp = self.client.get('/services/')
	# 	self.assertEqual(resp.status_code, 200)

	# def test_contact(self):
	# 	resp = self.client.get('/contact/')
	# 	self.assertEqual(resp.status_code, 200)

	# def test_contact(self):
	# 	resp = self.client.get('/about/')
	# 	self.assertEqual(resp.status_code, 200)

	# def test_contact(self):
	# 	resp = self.client.get('/terms_use/')
	# 	self.assertEqual(resp.status_code, 200)



	def test_bug(self):
		client = Client()
		
		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()
		# user1.save()
		response = client.post(reverse('login'),
									{'username':os.environ.get('reg_uname'),
									'password':os.environ.get('reg_pass')})

		print ["logged in "+ str(user1.id)]

		# import pdb;
		# pdb.set_trace()

		f = open() 

		projecttype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)

		status = BugStatus.objects.create(
			status_name = 'open'
			)

		project = ProductDetails.objects.create(
			prod_name = 'desktop',
			prod_type = projecttype.id,
			prod_version = '2',
			prod_description='sdfsdfsd',
			prod_file=File(open('/home/sachin/Desktop/templates.jpg','r'))

			)

		user = User.objects.create(
			username = 'sachin'
			)

		bug = BugDetails.objects.create(
				project_name= project,
				title=os.environ.get('title'),
				bug_type= bugtype,
				status= status,
				build_version=os.environ.get('version'),
				sprint_no= os.environ.get('sprintno'),
				dependent_module=os.environ.get('dependentmodule'),
				description=os.environ.get('description'),
				bug_owner=user,
				bug_assigned_to=user,
				bug_file=File(open('/home/sachin/Desktop/templates.jpg','r'))
			)

		data = {'project_name':os.environ.get('pname'),
				'title':os.environ.get('title'),
				'bug_type':os.environ.get('type'),
				'status':os.environ.get('status'),
				'build_version':os.environ.get('version'),
				'sprint_no':os.environ.get('sprintno'),
				'dependent_module':os.environ.get('dependentmodule'),
				'description':os.environ.get('description'),
				'bug_owner':os.environ.get('bugowner'),
				'bug_assigned_to':os.environ.get('bugassign'),
				'bug_file':os.environ.get('file')}

		print response
		print data

		form = Bug_Details_Form(data=data)
		self.assertTrue(form.is_valid())


		response = self.client.post(reverse('create_bug'),
				{'project_name':os.environ.get('pname'),
				'title':os.environ.get('title'),
				'bug_type':os.environ.get('type'),
				'status':os.environ.get('status'),
				'build_version':os.environ.get('version'),
				'sprint_no':os.environ.get('sprintno'),
				'dependent_module':os.environ.get('dependentmodule'),
				'description':os.environ.get('description'),
				'bug_owner':os.environ.get('bugowner'),
				'bug_assigned_to':os.environ.get('bugassign'),
				'bug_file':os.environ.get('file')})

		self.assertTrue(response.status_code,200)
		print response

	# def test_bug_fail(self):
	# 	client = Client()
	# 	response = self.client.post(reverse('create_bug'),
	# 			{'project_name':os.environ.get('pname'),
	# 			'title':os.environ.get('title'),
	# 			'bug_type':os.environ.get('type'),
	# 			'status':os.environ.get('status'),
	# 			'build_version':os.environ.get('version'),
	# 			'sprint_no':os.environ.get('sprintno'),
	# 			'dependent_module':os.environ.get('dependentmodule'),
	# 			'description':os.environ.get('description'),
	# 			'bug_owner':os.environ.get('bugowner'),
	# 			'bug_assigned_to':os.environ.get('bugassign'),
	# 			'bug_file':os.environ.get('file')})

	# 	print "Failed"
	# 	self.assertTrue(response.status_code,200)
