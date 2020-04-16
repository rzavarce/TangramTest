from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse

# Create your views here.
import json



def Index(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	return render(request, 'index.html',)



def LoginUsers(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.is_ajax() and request.method == "POST":

		print(request.POST)

		form = AuthenticationForm(data=request.POST)

		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				do_login(request, user)
				response = {"status":True,"msg":"paso todo OK"}
			else:
				response = {"status":False,"msg":"El usuario o contrasena invalida"}
		else:
			response = {"status":False,"msg":"el formulario no es valido"}
	else:
		response = {"status":False,"msg":"Ups a ocurrido un error"}


	return HttpResponse(json.dumps(response), content_type='application/json')   


def LogoutUsers(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """
	do_logout(request)
	return redirect('/')


def Dashboard(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		context={}
		context['menu_item'] = 'dashboard'
		return render(request, 'dashboard.html',context)

	return redirect('/')	











