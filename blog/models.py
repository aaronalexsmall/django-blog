from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)
	date_last_modified = models.DateTimeField(auto_now=True)
	date_published = models.DateTimeField(auto_now=True)
	published = models.BooleanField(default=False)

	def publish(self):
		self.published = True
		self.date_published = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title


