from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	
	class Meta:
		verbose_name_plural = 'Categories'
	
	def __str__(self): 
		return self.name
	# For Python 2, use __unicode__ too 
	def __unicode__(self):
		return self.name
	


class Page(models.Model):
	category = models.ForeignKey(Category) 
	title = models.CharField(max_length=128) 
	url = models.URLField()
	views = models.IntegerField(default=0)
	def __str__(self): 
		return self.title
	# For Python 2, use __unicode__ too 
	def __unicode__(self):
		return self.name