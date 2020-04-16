from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from .models import Article
from .forms import ArticleFormAdd, ArticleFormEdit


def ArticleList(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		context={}
		context['menu_item'] = 'articles'
		return render(request, 'articles/list.html',context)

	return redirect('/')	



def ArticleView(request, pk):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		context={}
		context['article'] = Article.objects.get(pk=pk)
		context['menu_item'] = 'articles'
		return render(request, 'articles/view.html', context)
	
	return redirect('/')	



def ArticleAdd(request):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		context={}
		context['form'] = ArticleFormAdd
		context['menu_item'] = 'articles'
		return render(request, 'articles/add.html',context)
	
	return redirect('/')	



def ArticleEdit(request, pk):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	if request.user.is_authenticated:
		context={}
		article = Article.objects.get(pk=pk)
		context['article_title'] = article.art_title 
		context['article_id'] = article.id
		context['form'] = ArticleFormEdit(instance=article)
		context['menu_item'] = 'articles'
		return render(request, 'articles/edit.html',context)
	
	return redirect('/')	



