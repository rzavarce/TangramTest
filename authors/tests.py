from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient


from .models import Author

import requests, json


class ArthorTestCase(APITestCase):
	
	def test_get_list(self):

		client = RequestsClient()
		response = client.get('http://127.0.0.1:8000/api/v1/authors/')
		assert response.status_code == 200

	def test_post_article(self):

		url='http://127.0.0.1:8000/api/v1/authors/'
		data= {"id":1,"aut_name":"prueba de author","aut_email":"xxxxxxx@tangram.com","aut_status":1}

		client = RequestsClient()
		response = client.post(url, data)

	def test_get_article(self):

		url='http://127.0.0.1:8000/api/v1/authors/1/'

		client = RequestsClient()
		response = client.get('http://127.0.0.1:8000/api/v1/articles/100/?format=json')


	def test_put_article(self):

		url='http://127.0.0.1:8000/api/v1/authors/1/	'
		data= {"id":1,"aut_name":"qqqq","aut_email":"prueba@tangram.com","aut_status":1}

		client = RequestsClient()
		response = client.put(url, data)

	def test_del_article(self):

		url='http://127.0.0.1:8000/api/v1/author/1/'

		client = RequestsClient()
		response = client.delete('http://127.0.0.1:8000/api/v1/articles/1/?format=json')




