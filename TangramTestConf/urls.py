"""TangramTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from manager import views as mng_views

from authors import viewsets as aut_viewsets
from authors import views as aut_views


router = routers.DefaultRouter()
router.register(r'authors', aut_viewsets.AuthorViewSet)



urlpatterns = [

	
	path('api/v1/', include(router.urls)),

	path('admin/', admin.site.urls),

	url(r'^$', mng_views.Index, name='index'),

	#url(r'^', include(router.urls)),



	#path('accounts/', include('django.contrib.auth.urls')),

	url('login/', mng_views.LoginUsers, name='login'),
	url('logout/', mng_views.LogoutUsers, name='logout'),
	url('dashboard/', mng_views.Dashboard, name='dashboard'),

	url('authors/add/', aut_views.AuthorAdd, name='authors_add'),
	url('authors/view/(?P<pk>[0-9]+)/', aut_views.AuthorView, name='autors_view'),
	url('authors/edit/(?P<pk>[0-9]+)/', aut_views.AuthorEdit, name='autors_edit'),
	#url('authors/delete/(?P<pk>[0-9]+)/', aut_views.AuthorDelete, name='autors_view'),
	url('authors/', aut_views.AuthorList, name='authors_list'),


	#url(r'^autors/(?P<pk>[0-9]+)/$', aut_views.AutorView, name='autors_view'),
	
	#url('autors/Edit/(?P<pk>[0-9]+)/', aut_views.AutorEdit, name='autors_edit'),



    


]










