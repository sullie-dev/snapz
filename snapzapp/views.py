from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html',  context)


def post(request, slug, *args, **kwargs):
    postQueryset = Post.objects.filter(slug=slug)
    post = get_object_or_404(postQueryset, slug=slug)
    comment = post.comments.filter(post=post).order_by("-created_on")
    context = {
        'posts': post,
        'comments': comment
    }
    print(comment)
    return render(request, 'post.html', context)
