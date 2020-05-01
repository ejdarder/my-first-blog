# we import the Post and Comment model defined in models.py
from django.contrib import admin
from .models import Post, Comment

# we need to make it visible on the admin page - we register it
admin.site.register(Post)
admin.site.register(Comment)
