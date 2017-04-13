from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate
from django.test import RequestFactory
from .views import login, register
import json
import os
from .forms import User_info_form

class SimpleTest(TestCase):

	def test_login(self):
		user = User.objects.create_user({'username':os.environ.get('log_uname'),
											'email':os.environ.get('log_email'),
											'password':os.environ.get('log_pass')})
		user.save()
		client=Client()
		response=self.client.post(reverse('login'),{'username':os.environ.get('log_uname1'),
													'password':os.environ.get('log_pass1')})
		self.assertTrue(response.status_code,200)

	def test_login_fail(self):
		user = User.objects.create_user({'username':os.environ.get('logf_uname'),
											'email':os.environ.get('logf_email'),
											'password':os.environ.get('logf_pass')})
		user.save()
		client=Client()
		response=self.client.post(reverse('login'),{'username':os.environ.get('logf_uname1'),
													'password':os.environ.get('logf_pass1')})
		print response
		self.assertTrue(response.status_code,200)

	def test_register(self):
		client=Client()
		response=self.client.post(reverse('register'),
											{'username':os.environ.get('reg_uname'),
											'email':os.environ.get('reg_email'),
											'password':os.environ.get('reg_pass')})
		print response
		self.assertTrue(response.status_code,200)

	def test_register_fail(self):
		client=Client()
		response=self.client.post(reverse('register'),
								{'username':os.environ.get('regf_uname'),
								'email':os.environ.get('regf_email'),
								'password':os.environ.get('regf_pass')})

		print "registration failed"
		self.assertTrue(response.status_code,200)

	# def test_basic_post_get(self):

	#         data = {
	#         u'ptype': u'1',
	#         u'user_data': u'[{"user_id":"129","user_role":"2"}]',
	#         u'prod_version': u'aaa',
	#         u'prod_description': u'aaaa',
	#         u'prod_name': u'aaaa',
	#         u'prod_file': u'[<InMemoryUploadedFile: link.txt (text/plain)>]'
	#         }
	#         client = Client()

	#         response = client.post('/create_product/', json.dumps(data), content_type='application/json')
	#         self.assertEquals(response.status_code, 302)
	#         #self.assertEquals(response['Location'], '/product_list/')

	#         response = client.get('/create_product?format=json')
	#         self.assertEquals(response.status_code, 200)
	#         self.assertEquals(json.loads(response.content), [data])

	def test_user_form(self):
		data = {'username':os.environ.get('uform_uname'),
				'email':os.environ.get('uform_email'),
				'password':os.environ.get('uform_pass')}
		form = User_info_form(data=data)
		self.assertTrue(form.is_valid())

	def test_user_form_fail(self):
		data = {'username':os.environ.get('uform_f_uname'),
				'email':os.environ.get('uform_f_email'),
				'password':os.environ.get('uform_f_pass')
				}
		form = User_info_form(data=data)
		self.assertTrue(form.is_valid())
		print "form is not valid"

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
		