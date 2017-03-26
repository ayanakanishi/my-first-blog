from django.db import models
from django.utils import timezone

# class Post(modelsModel) defines the model as an object
# class is the keyword that indicated we are defining an object
# Post is the name of the model
# models.Model means that the Post is a Django Model
class Post(models.Model):
	# The below are properties; define the type of the field (text, num, date, etc)
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(
		default=timezone.now)
	published_date=models.DateTimeField(
		blank=True, null=True)

# publish is the name of the method, should return something. 
	def publish(self):
		self.published_date=timezone.now()
		self.save()

# when you call the __str__ method, you get the post title back. 
	def __str__(self):
		return self.title

