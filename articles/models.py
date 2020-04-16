from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


# Create your models here.


STATUS = ((0,_('No Public')),(1,_('Public')))


class Article(models.Model):

	art_title = models.CharField(max_length=200, verbose_name=_('Title'))
	
	art_content = models.TextField(verbose_name=_('Content'))

	art_status = models.PositiveIntegerField(choices=STATUS, verbose_name=_('Status'),)

	art_created_date = models.DateTimeField(default=timezone.now, verbose_name=_('Creation Date'))
	art_modified_date = models.DateTimeField(default=timezone.now, verbose_name=_('Modification Date'))
	art_creator = models.ForeignKey(User, verbose_name=_('Creator'), on_delete=models.CASCADE)



	
	def __str__(self):
		return self.art_name


	class Meta:
	    verbose_name = _('Article')
	    verbose_name_plural = _('Articles')







