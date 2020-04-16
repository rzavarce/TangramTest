from django import forms

from .models import Author



class AuthorFormAdd(forms.ModelForm):

	class Meta:
		model = Author
		fields = ['aut_name', 'aut_email', 'aut_status',]




class AuthorFormEdit(forms.ModelForm):

	class Meta:
		model = Author
		fields = ['aut_name', 'aut_email', 'aut_status',]



