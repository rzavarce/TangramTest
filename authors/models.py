from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


# Create your models here.


STATUS = ((0,_('Pending')),(1,_('Active')))


class Author(models.Model):
	"""
    API endpoint that allows users to be viewed or edited.
    """

	aut_name = models.CharField(max_length=150, verbose_name=_('Fullname'))
	
	aut_email = models.EmailField(verbose_name=_('Email'))

	aut_status = models.PositiveIntegerField(choices=STATUS, verbose_name=_('Status'),)

	aut_created_date = models.DateTimeField(default=timezone.now, verbose_name=_('Creation Date'))
	aut_modified_date = models.DateTimeField(default=timezone.now, verbose_name=_('Modification Date'))
	aut_creator = models.ForeignKey(User, verbose_name=_('Creator'), on_delete=models.CASCADE)


	
	def __str__(self):
		return self.aut_name


	class Meta:
	    verbose_name = _('Author')
	    verbose_name_plural = _('Authors')






