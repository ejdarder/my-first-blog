from django.shortcuts import render

# we create a function called post_list that takes
# request and will return the value it gets from calling another
# function named render that will render our template
def post_list(request):
	return render(request, 'blog/post_list.html', {})