from django import forms

from .models import Article



class ArticleFormAdd(forms.ModelForm):

	class Meta:
		model = Article
		fields = ['art_title', 'art_content', 'art_status',]




class ArticleFormEdit(forms.ModelForm):

	class Meta:
		model = Article
		fields = ['art_title', 'art_content', 'art_status',]



