from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # class is a keyword to define objects, we are defining a model named Post
# !!!! Always start a class name with an uppercase
# Django knows Post it's a Django Model that needs to be saved in the db

# Every object has properties and methods
# Properties definition - defining the type of each property: text, number, date
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

# Methods definition- they are both indented inside the class
# publish is something we can do to the object Post
	def published(self):
		self.published_date=timezone.now()
		self.save()

# methods often return something
# here we will get a string with a Post title
	def __str__(self):
		return self.title
