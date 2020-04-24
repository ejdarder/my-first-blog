# we import the Post model defined in models.py
from django.contrib import admin
from .models import Post

# we need to make it visible on the admin page - we register it
admin.site.register(Post)