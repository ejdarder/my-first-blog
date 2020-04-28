from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# we create a function called post_list that takes
# request and will return the value it gets from calling another
# function named render that will render our template
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})