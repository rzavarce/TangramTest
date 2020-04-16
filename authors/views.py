from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from .models import Author
from .forms import AuthorFormAdd, AuthorFormEdit


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
		context={}
		context['author'] = Author.objects.get(pk=pk)
		return render(request, 'authors/view.html', context)
	
	return redirect('/')	



def AuthorAdd(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		context={}
		context['form'] = AuthorFormAdd
		return render(request, 'authors/add.html',context)
	
	return redirect('/')	



def AuthorEdit(request, pk):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		context={}
		author = Author.objects.get(pk=pk)
		context['author_name'] = author.aut_name 
		context['author_id'] = author.id
		context['form'] = AuthorFormEdit(instance=author)
		return render(request, 'authors/edit.html',context)
	
	return redirect('/')	



