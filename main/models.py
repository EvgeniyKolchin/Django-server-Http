from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IBeacon(models.Model):
	minor = models.IntegerField(null=False, blank=False)
	major = models.IntegerField(null=False, blank=False)
	image = models.ImageField()

	def __unicode__(self):
		return "{self.major}:{self.minor}".format(self=self)
