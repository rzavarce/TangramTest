from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from .models import Author



def AuthorList(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		return render(request, 'authors/list.html',)

	return redirect('/')	



def AuthorView(request, pk):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		return render(request, 'authors/view.html',)
	
	return redirect('/')	





def AuthorEdit(request, pk):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		return render(request, 'authors/edit.html',)
	
	return redirect('/')	



