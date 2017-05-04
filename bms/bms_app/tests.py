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
from .models import BugDetails, ProductDetails, BugType, BugStatus, ProjectType, ProductUser, UserRole, Comments
from .forms import User_info_form, Bug_Details_Form, comment_form
from django.core.files import File
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import UserManager, AbstractUser

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

		ptype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)

		status = BugStatus.objects.create(
			status_name = 'open'
			)

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

		form = Bug_Details_Form(data=data)
		self.assertTrue(form.is_valid())
		print "form is valid ===>", form.is_valid()

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

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)

		status = BugStatus.objects.create(
			status_name = 'open'
			)

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

		form = Bug_Details_Form(data=data)
		self.assertFalse(form.is_valid())
		print "form is valid ===>", form.is_valid()


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

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)

		status = BugStatus.objects.create(
			status_name = 'open'
			)

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
			'project_name':os.environ.get('projname'),
			'prod_type': os.environ.get('projtype'),
			'prod_user': os.environ.get('produser'),
			'prod_user_role': os.environ.get('userrole'),
			'prod_version': os.environ.get('version'),
			'prod_description':os.environ.get('description')
		})

		self.assertTrue(response.status_code, 200)
		print response


	def test_comment_section(self):

		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()

		response = self.client.post(reverse('comment_section'),
		{
			'comment_text':os.environ.get('comment'),
			'bid': os.environ.get('bid'),
			'userid': os.environ.get('uid')
		})

		self.assertTrue(response.status_code, 200)
		print response

	def test_comment_query(self):
		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()

		ptype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)

		status = BugStatus.objects.create(
			status_name = 'open'
			)

		p = ProductDetails.objects.create(
			prod_name='bugmanagement',
			prod_type=ptype
			)

		bug = BugDetails.objects.create(
				project_name= p,
				title='bug',
				bug_type= bugtype,
				status= status,
				build_version=2,
				sprint_no= 2,
				dependent_module='project',
				description='project',
				bug_owner=user1,
				bug_assigned_to=user1
			)
		comment = Comments.objects.create(
			    user = user1,
    			bug = bug,
    			comment = 'nice'
			)

		
		comment = Comments.objects.get(pk=1)
		print "comment===>",comment
		post_comment = Comments.objects.filter(bug=1)
		print "post comment==>",post_comment
		self.assertQuerysetEqual(post_comment, ['<Comments: nice>'])


	def test_comment_form(self):
		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()

		ptype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)

		status = BugStatus.objects.create(
			status_name = 'open'
			)

		p = ProductDetails.objects.create(
			prod_name='bugmanagement',
			prod_type=ptype
			)

		bug = BugDetails.objects.create(
				project_name= p,
				title='bug',
				bug_type= bugtype,
				status= status,
				build_version=2,
				sprint_no= 2,
				dependent_module='project',
				description='project',
				bug_owner=user1,
				bug_assigned_to=user1
			)
		comment = Comments.objects.create(
			    user = user1,
    			bug = bug,
    			comment = 'nice'
			)
		data = {'comment':os.environ.get('comment'),
				'user':os.environ.get('userid'),
				'bug':os.environ.get('bugid')}
		form = comment_form(data=data)
		print "form error==>",form.errors
		self.assertFalse(form.is_valid())
		
	def test_comment_form_fail(self):
		user1=User.objects.create(username=os.environ.get('reg_uname'),
		 							email=os.environ.get('reg_email'),
		 							password=os.environ.get('reg_pass'),
		 							is_active=True)
 		user1.set_password(os.environ.get('reg_pass'))
		user1.save()

		ptype = ProjectType.objects.create(
			project_type_name= 'mobile'
			)

		bugtype = BugType.objects.create(
			bug_name = 'bug'
			)

		status = BugStatus.objects.create(
			status_name = 'open'
			)

		p = ProductDetails.objects.create(
			prod_name='bugmanagement',
			prod_type=ptype
			)

		bug = BugDetails.objects.create(
				project_name= p,
				title='bug',
				bug_type= bugtype,
				status= status,
				build_version=2,
				sprint_no= 2,
				dependent_module='project',
				description='project',
				bug_owner=user1,
				bug_assigned_to=user1
			)
		comment = Comments.objects.create(
			    user = user1,
    			bug = bug,
    			comment = 'nice'
			)
		data = {
				'user':os.environ.get('userid')
					}
		form = comment_form(data=data)
		self.assertFalse(form.is_valid())
		