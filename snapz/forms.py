from snapzapp.models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'description')
