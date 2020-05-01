from django import forms
from .models import Post, Comment

# Adding a form to post posts on blog
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# Adding a form to post comments on blog
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)