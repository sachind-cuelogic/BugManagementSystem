from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate
from django.test import RequestFactory
from .views import login, register, create_bug, bug_list
import json
import os
from .models import BugDetails, ProductDetails, BugType, BugStatus, ProjectType, ProductUser, UserRole
from .forms import User_info_form, Bug_Details_Form
from django.core.files import File
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse


class SimpleTest(TestCase):

	def test_register(self):
		client = Client()
		response = self.client.post(reverse('register'),
									{'username':os.environ.get('reg_uname'),
									'email':os.environ.get('reg_email'),
									'password':os.environ.get('reg_pass')})
		print response
		self.assertTrue(response.status_code,200)


	def test_user_form(self):
		data = {'username':os.environ.get('uform_uname'),
				'email':os.environ.get('uform_email'),
				'password':os.environ.get('uform_pass')}
		form = User_info_form(data=data)
		self.assertTrue(form.is_valid())


	def test_user_form_fail(self):
		user =User.objects.create(username=os.environ.get('uform_f_uname'), password='')
		data = {'username': user.username, 'password': user.password,}
		form = User_info_form(data=data)
		self.assertFalse(form.is_valid())


	def test_login(self):
		client = Client()
		response = client.post(reverse('register'),
									{'username':os.environ.get('reg_uname'),
									'email':os.environ.get('reg_email'),
									'password':os.environ.get('reg_pass')})
		response = client.post(reverse('login'),
									{'username':os.environ.get('reg_uname'),
									'password':os.environ.get('reg_pass')})
		print response
		self.assertTrue(response.status_code,200)

	def test_login_fail(self):
		client = Client()
		response = client.post(reverse('register'),
									{'username':os.environ.get('logf_uname'),
									'email':os.environ.get('logf_email'),
									'password':os.environ.get('logf_pass')})
		response = client.post(reverse('login'),
									{'username':os.environ.get('logf_uname1'),
									'password':os.environ.get('logf_pass1')})
		print response
		self.assertTrue(response.status_code,200)


	def test_register_fail(self):
		user = User.objects.create_user({'username':os.environ.get('log_uname'),
									'email':os.environ.get('log_email'),
									'password':os.environ.get('log_pass')})
		user.save()
		client = Client()
		response = self.client.post(reverse('register'),
								{'username':os.environ.get('regf_uname'),
								'password':os.environ.get('regf_pass')})
		self.assertTrue(response.status_code,200)


	def test_landing_page(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_website_home(self):
		resp = self.client.get('/website_home/')
		self.assertEqual(resp.status_code, 200)

	def test_services(self):
		resp = self.client.get('/services/')
		self.assertEqual(resp.status_code, 200)

	def test_contact(self):
		resp = self.client.get('/contact/')
		self.assertEqual(resp.status_code, 200)

	def test_contact(self):
		resp = self.client.get('/about/')
		self.assertEqual(resp.status_code, 200)

	def test_contact(self):
		resp = self.client.get('/terms_use/')
		self.assertEqual(resp.status_code, 200)



	def test_bug(self):
		client = Client()
		
		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()

		response = client.post(reverse('login'),
									{'username':os.environ.get('reg_uname'),
									'password':os.environ.get('reg_pass')})

		print ["logged in "+ str(user1.id)]

<<<<<<< HEAD
=======
		# import pdb;
		# pdb.set_trace()

>>>>>>> 4aea892f7a431f7f214a47a4a945b5e67448ac35
		ptype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)
		print ptype

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)
		print bugtype

		status = BugStatus.objects.create(
			status_name = 'open'
			)
		print status

		p = ProductDetails.objects.create(
			prod_name='bugmanagement',
			prod_type=ptype
			)

		bug = BugDetails.objects.create(
				project_name= p,
				title=os.environ.get('title'),
				bug_type= bugtype,
				status= status,
				build_version=os.environ.get('version'),
				sprint_no= os.environ.get('sprintno'),
				dependent_module=os.environ.get('dependentmodule'),
				description=os.environ.get('description'),
				bug_owner=user1,
				bug_assigned_to=user1
			)

		print bug

		data = {'project_name':os.environ.get('pname'),
				'title':os.environ.get('title'),
				'bug_type':os.environ.get('type'),
				'status':os.environ.get('status'),
				'build_version':os.environ.get('version'),
				'sprint_no':os.environ.get('sprintno'),
				'dependent_module':os.environ.get('dependentmodule'),
				'description':os.environ.get('description'),
				'bug_owner':os.environ.get('bugowner'),
				'bug_assigned_to':os.environ.get('bugassign')}

		print response
		print data

		form = Bug_Details_Form(data=data)
		print "--->",form.errors
		self.assertTrue(form.is_valid())
		print "===>", form.is_valid()
<<<<<<< HEAD

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
				'bug_file':os.environ.get('file')}
				)

		self.assertTrue(response.status_code,200)
		print response

	def test_bug_fail(self):
		client = Client()
		
		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()
		response = client.post(reverse('login'),
									{'username':os.environ.get('reg_uname'),
									'password':os.environ.get('reg_pass')})

		print ["logged in "+ str(user1.id)]

		ptype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)
		print ptype

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)
		print bugtype

		status = BugStatus.objects.create(
			status_name = 'open'
			)
		print status

		p = ProductDetails.objects.create(
			prod_name='bugmanagement',
			prod_type=ptype
			)

		bug = BugDetails.objects.create(
				project_name= p,
				title=os.environ.get('title'),
				bug_type= bugtype,
				status= status,
				build_version=os.environ.get('version'),
				sprint_no= os.environ.get('sprintno'),
				dependent_module=os.environ.get('dependentmodule'),
				description=os.environ.get('description'),
				bug_owner=user1,
				bug_assigned_to=user1
			)

		print bug

		data = {'project_name':os.environ.get('pname'),
				'title':os.environ.get('title'),
				'bug_type':os.environ.get('type'),
				'status':os.environ.get('status'),
				'build_version':os.environ.get('version'),
				'sprint_no':os.environ.get('sprintno'),
				'dependent_module':os.environ.get('dependentmodule'),
				'description':os.environ.get('description'),
				'bug_owner':os.environ.get('bugowner')
				}

		print response
		print data

		form = Bug_Details_Form(data=data)
		print "--->",form.errors
		self.assertFalse(form.is_valid())
		print "===>", form.is_valid()
=======
>>>>>>> 4aea892f7a431f7f214a47a4a945b5e67448ac35

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
				'bug_file':os.environ.get('file')}
				)

		self.assertTrue(response.status_code,200)
		print response

 	def test_create_project(self):
		client = Client()
		
		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()

		response = client.post(reverse('login'),
									{'username':os.environ.get('reg_uname'),
									'password':os.environ.get('reg_pass')})

		print ["logged in "+ str(user1.id)]

		ptype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)
		print ptype

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)
		print bugtype

		status = BugStatus.objects.create(
			status_name = 'open'
			)
		print status

		p = ProductDetails.objects.create(
			prod_name='bugmanagement',
			prod_type=ptype
			)

		ur = UserRole.objects.create(
			role = 'engineer'
			)

		pu = ProductUser.objects.create(
			prod_user=user1,
			product=p,
			prod_user_role=ur
			)

		response = self.client.post(reverse('create_project'),
		{
			'project_name':os.environ.get('pname'),
			'prod_type': os.environ.get('projtype'),
			'prod_user': os.environ.get('produser'),
			'prod_user_role': os.environ.get('userrole'),
			'prod_version': os.environ.get('version'),
			'prod_description':os.environ.get('description')
			'user_data':
						{'user_id':os.environ.get('produser'),
						'user_role':os.environ.get('userrole')}
		}
		
		)

		self.assertTrue(response.status_code, 200)
		print response








#--------------------------------------------------------------------

	# def test_bug_list(self):
	# 	client = Client()
		
	# 	user1=User.objects.create(username=os.environ.get('reg_uname'),
	# 		email=os.environ.get('reg_email'),
	# 		password=os.environ.get('reg_pass'),
	# 		is_active=True)
	# 	user1.set_password(os.environ.get('reg_pass'))
	# 	user1.save()
	# 	# user1.save()
	# 	response = client.post(reverse('login'),
	# 		{'username':os.environ.get('reg_uname'),
	# 		'password':os.environ.get('reg_pass')})

	# 	print ["logged in "+ str(user1.id)]

	# 	ptype = ProjectType.objects.create(
	# 		project_type_name= 'mobile'
	# 		)
	# 	print ptype

	# 	pd = ProductDetails.objects.create(
	# 		prod_name='bugmanagement',
	# 		prod_type=ptype,
	# 		prod_version='2'
	# 		)

	# 	ur = UserRole.objects.create(
	# 		role = 'engineer'
	# 		)

	# 	pu = ProductUser.objects.create(
	# 		prod_user=user1,
	# 		product=pd,
	# 		prod_user_role=ur
	# 		)

	# 	# self.factory = RequestFactory()
	# 	# request = self.factory.get('/bug_list/?pid=1')

	# 	# response = self.client.post(reverse('bug_list',request),
	# 	# 		{}
	# 	# 		)


	# 	self.factory = RequestFactory()

	# 	request = self.factory.get(reverse('/bug_list/?pid=1'))

	# 	response = bug_list(request)

	# 	self.assertEqual(response.status_code, 200)
	# 	print response



	# def test_that_user_gets_logged_in(self):
	# 	client = Client()
<<<<<<< HEAD
	# 	user1=User.objects.create(username=os.environ.get('reg_uname'),
	# 	 							email=os.environ.get('reg_email'),
	# 	 							password=os.environ.get('reg_pass'),
	# 	 							is_active=True)
 # 		user1.set_password(os.environ.get('reg_pass'))
	# 	user1.save()

	# 	response = self.client.post(reverse('register'),
	# 								{'username':os.environ.get('reg_uname'),
	# 								'email':os.environ.get('reg_email'),
	# 								'password':os.environ.get('reg_pass')})
	# 	print response

 #    	user = User.objects.get(username='mahesh')
 #    	assert user.is_authenticated()


 	# def test_create_project(self):
		# client = Client()
		
		# user1=User.objects.create(username=os.environ.get('reg_uname'),
		#  							email=os.environ.get('reg_email'),
		#  							password=os.environ.get('reg_pass'),
		#  							is_active=True)
 	# 	user1.set_password(os.environ.get('reg_pass'))
		# user1.save()
		# # user1.save()

 	# 	self.client.login(username=os.environ.get('reg_uname'),
 	# 						 password=os.environ.get('reg_pass'))

		# # response = client.post(reverse('login'),
		# # 							{'username':os.environ.get('reg_uname'),
		# # 							'password':os.environ.get('reg_pass')})

		# print ["logged in "+ str(user1.id)]

		# # import pdb;
		# # pdb.set_trace()

		# ptype = ProjectType.objects.create(
		# 	project_type_name= 'mobile'
		# 	)
		# print ptype

		# bugtype = BugType.objects.create(
		# 	bug_name = 'bug'
		# 	)
		# print bugtype

		# status = BugStatus.objects.create(
		# 	status_name = 'open'
		# 	)
		# print status

		# p = ProductDetails.objects.create(
		# 	prod_name='bugmanagement',
		# 	prod_type=ptype
		# 	)

		# ur = UserRole.objects.create(
		# 	role = 'engineer'
		# 	)

		# pu = ProductUser.objects.create(
		# 	prod_user=user1,
		# 	product=p,
		# 	prod_user_role=ur
		# 	)


		# response = self.client.post(reverse('create_project'),
		# {
		# 	'project_name':os.environ.get('pname'),
		# 	'prod_type': os.environ.get('projtype'),
		# 	'prod_user': os.environ.get('produser'),
		# 	'prod_user_role': os.environ.get('userrole'),
		# 	'prod_version': os.environ.get('version'),
		# 	'prod_description':os.environ.get('description')
		# 	'user_data':
		# 				{'user_id':os.environ.get('produser'),
		# 				'user_role':os.environ.get('userrole')}
		# }
		
		# )

		# self.assertTrue(response.status_code, 200)
		# print response
=======
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

	# 	self.assertTrue(response.status_code,200)
>>>>>>> 4aea892f7a431f7f214a47a4a945b5e67448ac35
