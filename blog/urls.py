# import Django's function path
from django.urls import path
# import all views from the blog application
from . import views

# add first URL pattern
urlpatterns = [
	path('', views.post_list, name='post_list'),
] # we just assigned a view called post_list to the root URL