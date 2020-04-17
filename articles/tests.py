from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient

from .models import Article

import requests, json


from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from django.urls import reverse


class ArticleTestCase(APITestCase):
	
	def test_get_list(self):

		client = RequestsClient()
		response = client.get('http://127.0.0.1:8000/api/v1/articles/')
		assert response.status_code == 200

	def test_post_article(self):

		url='http://127.0.0.1:8000/api/v1/articles/'
		data= {"id":100,"art_title":"Esta es una prueba","art_content":"Esta es una prueba y su contenido","art_status":1}

		client = RequestsClient()
		response = client.post(url, data)

	def test_get_article(self):

		url='http://127.0.0.1:8000/api/v1/articles/1/'

		client = RequestsClient()
		response = client.get('http://127.0.0.1:8000/api/v1/articles/1/?format=json')


	def test_put_article(self):

		url='http://127.0.0.1:8000/api/v1/articles/1/	'
		data= {"id":1,"art_title":"qwqwqwqw111111","art_content":"qwqwqwqwqw","art_status":1}

		client = RequestsClient()
		response = client.put(url, data)

	def test_del_article(self):

		url='http://127.0.0.1:8000/api/v1/articles/1/'

		client = RequestsClient()
		response = client.delete('http://127.0.0.1:8000/api/v1/articles/1/?format=json')


